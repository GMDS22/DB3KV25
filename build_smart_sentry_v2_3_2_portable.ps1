param(
    [switch]$IncludeModels,
    [switch]$IncludeSklearn,
    [switch]$IncludeYtDlp,
    [switch]$ExcludeModels,
    [switch]$ExcludeSklearn,
    [switch]$ExcludeYtDlp,
    [string]$OutputDrive = 'F:',
    [switch]$Clean
)

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $repoRoot

function Stop-ReleaseProcesses([string]$targetRoot) {
    $normalizedRoot = [System.IO.Path]::GetFullPath($targetRoot)
    Get-Process | ForEach-Object {
        try {
            $processPath = $_.Path
            if ($processPath) {
                $normalizedProcessPath = [System.IO.Path]::GetFullPath($processPath)
                if ($normalizedProcessPath.StartsWith($normalizedRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
                    Stop-Process -Id $_.Id -Force -ErrorAction SilentlyContinue
                }
            }
        } catch {
        }
    }
}

function Remove-DirectoryRobust([string]$targetPath) {
    if (-not (Test-Path $targetPath)) {
        return
    }
    Stop-ReleaseProcesses $targetPath
    try {
        Remove-Item $targetPath -Recurse -Force -ErrorAction Stop
        return
    } catch {
    }

    $item = Get-Item $targetPath -Force -ErrorAction SilentlyContinue
    if ($null -ne $item -and -not $item.PSIsContainer) {
        cmd /c "attrib -R \"$targetPath\" >nul 2>&1"
        cmd /c "del /f /q \"$targetPath\""
        if (Test-Path $targetPath) {
            throw "Unable to remove file: $targetPath"
        }
        return
    }

    $quotedPath = '"' + $targetPath + '"'
    cmd /c "attrib -R $quotedPath\* /S /D >nul 2>&1"
    cmd /c "rd /s /q $quotedPath"
    if (Test-Path $targetPath) {
        throw "Unable to remove directory: $targetPath"
    }
}

function Get-ActiveVersion {
    foreach ($versionName in @(
        'SMART_SENTRY_V3_0_VERSION.txt',
        'SMART_SENTRY_V2_3_2_VERSION.txt',
        'SMART_SENTRY_V2_3_1_VERSION.txt',
        'SMART_SENTRY_V2_0_VERSION.txt'
    )) {
        $versionPath = Join-Path $repoRoot $versionName
        if (Test-Path $versionPath) {
            $raw = (Get-Content $versionPath -Raw).Trim().TrimStart('v', 'V')
            if ($raw) {
                return $raw
            }
        }
    }
    return '2.3.2'
}

function Get-ActiveVersionMetadata {
    foreach ($versionName in @(
        'SMART_SENTRY_V3_0_VERSION.txt',
        'SMART_SENTRY_V2_3_2_VERSION.txt',
        'SMART_SENTRY_V2_3_1_VERSION.txt',
        'SMART_SENTRY_V2_0_VERSION.txt'
    )) {
        $versionPath = Join-Path $repoRoot $versionName
        if (-not (Test-Path $versionPath)) {
            continue
        }

        $rawVersion = (Get-Content $versionPath -Raw).Trim().TrimStart('v', 'V')
        if (-not $rawVersion) {
            continue
        }

        return [PSCustomObject]@{
            Version = $rawVersion
            MarkerPath = $versionPath
        }
    }

    return [PSCustomObject]@{
        Version = '2.3.2'
        MarkerPath = (Join-Path $repoRoot 'SMART_SENTRY_V2_3_2_VERSION.txt')
    }
}

function Test-DriveRootAvailable([string]$driveRoot) {
    $trimmed = $driveRoot.Trim()
    if (-not $trimmed) {
        return $false
    }
    $probePath = if ($trimmed.EndsWith('\')) { "${trimmed}NUL" } else { "$trimmed\NUL" }
    cmd /c "if exist $probePath (exit 0) else (exit 1)" | Out-Null
    return ($LASTEXITCODE -eq 0)
}

function Assert-RequiredReleaseArtifacts([string]$buildRoot, [string]$exeName, [string]$contentsDirName, [string]$pythonRuntimeDllName, [string[]]$requiredContentRelativePaths = @()) {
    $contentsDirPath = Join-Path $buildRoot $contentsDirName
    $requiredPaths = @(
        (Join-Path $buildRoot $exeName),
        $contentsDirPath,
        (Join-Path $contentsDirPath 'base_library.zip'),
        (Join-Path $contentsDirPath 'python3.dll'),
        (Join-Path $contentsDirPath $pythonRuntimeDllName)
    )

    foreach ($relativePath in $requiredContentRelativePaths) {
        if ([string]::IsNullOrWhiteSpace($relativePath)) {
            continue
        }
        $requiredPaths += (Join-Path $contentsDirPath $relativePath)
    }

    $missingPaths = @($requiredPaths | Where-Object { -not (Test-Path $_) })
    if ($missingPaths.Count -gt 0) {
        $missingList = ($missingPaths | ForEach-Object { " - $_" }) -join [Environment]::NewLine
        throw "PyInstaller staging output is incomplete. Missing required runtime artifacts:`n$missingList`nStaged build was left in place for inspection: $buildRoot"
    }
}

function Assert-PythonModulesAvailable([string]$pythonCommand, [string[]]$moduleNames) {
    foreach ($moduleName in $moduleNames) {
        & $pythonCommand -c "import importlib.util, sys; sys.exit(0 if importlib.util.find_spec('$moduleName') else 1)"
        if ($LASTEXITCODE -ne 0) {
            throw "Required Python package is not installed in the local build environment: $moduleName"
        }
    }
}

function Set-PackagedYoloConfig([string]$configPath, [string]$modelDir) {
    if (-not (Test-Path $configPath)) {
        return
    }
    $configData = Get-Content $configPath -Raw | ConvertFrom-Json
    if ($null -eq $configData.detection_mode) {
        return
    }
    $configData.detection_mode.yolo_model_dir = $modelDir
    $configData | ConvertTo-Json -Depth 100 | Set-Content -Path $configPath -Encoding UTF8
}

function Set-PackagedConfigSurface([string]$configPath, [string]$settingsRelativePath, [string]$promptedRelativePath, [string]$faceRelativePath, [string]$modelDir, [string]$udpHost, [int]$udpPort) {
    if (-not (Test-Path $configPath)) {
        return
    }

    $configData = Get-Content $configPath -Raw | ConvertFrom-Json

    if ($null -ne $configData.detection_mode) {
        $configData.detection_mode.yolo_model_dir = $modelDir
    }
    if ($null -ne $configData.connection) {
        $configData.connection.udp_host = $udpHost
        $configData.connection.udp_port = $udpPort
    }
    if ($null -eq $configData.face_recognition) {
        $configData | Add-Member -NotePropertyName face_recognition -NotePropertyValue ([pscustomobject]@{})
    }
    if ($configData.face_recognition -isnot [psobject]) {
        $configData.face_recognition = [pscustomobject]@{}
    }
    $faceLibraryProperty = $configData.face_recognition.PSObject.Properties.Match('library_path')
    if ($null -eq $faceLibraryProperty -or $faceLibraryProperty.Count -eq 0) {
        $configData.face_recognition | Add-Member -NotePropertyName library_path -NotePropertyValue $faceRelativePath -Force
    } else {
        $configData.face_recognition.library_path = $faceRelativePath
    }

    $configData.prompted_library_path = $promptedRelativePath
    $configData.config_path = $settingsRelativePath
    $configData | ConvertTo-Json -Depth 100 | Set-Content -Path $configPath -Encoding UTF8
}

function Patch-BundledUltralyticsGit([string]$contentsDirPath) {
    $gitPyPath = Join-Path $contentsDirPath 'ultralytics\utils\git.py'
    if (-not (Test-Path $gitPyPath)) {
        throw "Expected bundled ultralytics git module was not found: $gitPyPath"
    }

    $riskyToken = 'path: Path = Path(__file__).resolve()'
    $safeToken = 'path: Path = Path(".")'
    $raw = Get-Content $gitPyPath -Raw

    if ($raw.Contains($safeToken) -and -not $raw.Contains($riskyToken)) {
        Write-Host "Bundled ultralytics git.py already hardened: $gitPyPath"
        return
    }

    if (-not $raw.Contains($riskyToken)) {
        throw "Unable to apply ultralytics hardening patch; expected token was not found in: $gitPyPath"
    }

    $patched = $raw.Replace($riskyToken, $safeToken)
    Set-Content -Path $gitPyPath -Value $patched -Encoding UTF8

    $verify = Get-Content $gitPyPath -Raw
    if ($verify.Contains($riskyToken) -or -not $verify.Contains($safeToken)) {
        throw "Bundled ultralytics hardening patch verification failed: $gitPyPath"
    }

    Write-Host "Applied bundled ultralytics hardening patch: $gitPyPath"
}

function Copy-ReleaseConfigAlias([string]$sourcePath, [string]$targetPath) {
    if (-not (Test-Path $sourcePath)) {
        return
    }
    $targetDir = Split-Path -Parent $targetPath
    if ($targetDir) {
        New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
    }
    Copy-Item -Path $sourcePath -Destination $targetPath -Force
}

function Remove-ReleaseConfigAlias([string]$targetPath) {
    if (Test-Path $targetPath) {
        Remove-Item $targetPath -Force -ErrorAction SilentlyContinue
    }
}

function Sync-QtVcRuntimeDllsAtPath([string]$qtBinDir) {
    if (-not (Test-Path $qtBinDir)) {
        return
    }

    $runtimeNames = @(
        'msvcp140.dll',
        'msvcp140_1.dll',
        'msvcp140_2.dll',
        'vcruntime140.dll',
        'vcruntime140_1.dll'
    )

    foreach ($runtimeName in $runtimeNames) {
        $systemRuntimePath = Join-Path $env:WINDIR "System32\$runtimeName"
        if (-not (Test-Path $systemRuntimePath)) {
            continue
        }
        Copy-Item -Path $systemRuntimePath -Destination (Join-Path $qtBinDir $runtimeName) -Force
    }
}

function Sync-BuildQtVcRuntimeDlls([string]$pythonExePath) {
    if ([string]::IsNullOrWhiteSpace($pythonExePath) -or -not (Test-Path $pythonExePath)) {
        return
    }

    $pythonDir = Split-Path $pythonExePath -Parent
    $pythonRoot = Split-Path $pythonDir -Parent
    $qtBinDir = Join-Path $pythonRoot 'Lib\site-packages\PyQt5\Qt5\bin'
    Sync-QtVcRuntimeDllsAtPath $qtBinDir
}

function Sync-QtVcRuntimeDlls([string]$releaseRoot, [string]$contentsDirName) {
    $qtBinDir = Join-Path $releaseRoot "$contentsDirName\PyQt5\Qt5\bin"
    Sync-QtVcRuntimeDllsAtPath $qtBinDir
}

function Invoke-NativeProcess([string]$filePath, [string[]]$arguments, [string]$workingDirectory) {
    $quotedArguments = $arguments | ForEach-Object {
        if ($_ -match '[\s;\"]') {
            '"' + (($_ -replace '(\\*)"', '$1$1\\"') -replace '(\\+)$', '$1$1') + '"'
        } else {
            $_
        }
    }

    $process = Start-Process -FilePath $filePath -ArgumentList ($quotedArguments -join ' ') -WorkingDirectory $workingDirectory -NoNewWindow -Wait -PassThru
    return $process.ExitCode
}

$activeVersionMetadata = Get-ActiveVersionMetadata
$activeVersion = $activeVersionMetadata.Version
$activeVersionToken = $activeVersion -replace '\.', '_'
$activeLauncherModule = "app.main"
$activeLauncherPath = Join-Path $repoRoot "app\main.py"
$releaseDir = Join-Path $OutputDrive "SMART SENTRY V$activeVersion"
$releaseExeBase = "SMART_SENTRY_V$activeVersion"
$releaseExeName = "$releaseExeBase.exe"
$releaseContentsDirName = "SMART_SENTRY_V${activeVersionToken}_FILES"
$legacyBuildRoot = Join-Path $repoRoot 'build'
$pyInstallerTempRoot = Join-Path (Split-Path $repoRoot -Parent) '.pyinstaller-temp'
$distRoot = Join-Path $pyInstallerTempRoot 'dist'
$workRoot = Join-Path $pyInstallerTempRoot 'work'
$specRoot = Join-Path $pyInstallerTempRoot 'spec'
$stagingDir = Join-Path $distRoot $releaseExeBase

$workspacePython311 = Join-Path (Split-Path $repoRoot -Parent) '.venv311\Scripts\python.exe'
$repoPython311 = Join-Path $repoRoot '.venv311\Scripts\python.exe'
$workspacePython = Join-Path (Split-Path $repoRoot -Parent) '.venv\Scripts\python.exe'
$repoPython = Join-Path $repoRoot '.venv\Scripts\python.exe'
$overridePython = $env:SMART_SENTRY_PYTHON_EXE
$pythonExe = $overridePython
if ([string]::IsNullOrWhiteSpace($pythonExe) -or -not (Test-Path $pythonExe)) {
    $pythonExe = $workspacePython311
}
if (-not (Test-Path $pythonExe)) {
    $pythonExe = $repoPython311
}
if (-not (Test-Path $pythonExe)) {
    $pythonExe = $workspacePython
}
if (-not (Test-Path $pythonExe)) {
    $pythonExe = $repoPython
}
if (-not (Test-Path $pythonExe)) {
    $pythonExe = 'python'
}

Sync-BuildQtVcRuntimeDlls -pythonExePath $pythonExe

$pythonRuntimeDllName = (& $pythonExe -c "import sys; print(f'python{sys.version_info.major}{sys.version_info.minor}.dll')").Trim()
if (-not $pythonRuntimeDllName) {
    throw 'Unable to determine the Python runtime DLL name for the selected interpreter.'
}

$cv2DataPath = (& $pythonExe -c "import cv2, pathlib; print(pathlib.Path(cv2.__file__).resolve().parent / 'data')").Trim()

$bundleModels = -not $ExcludeModels
$bundleSklearn = $IncludeSklearn -and -not $ExcludeSklearn
$bundleYtDlp = $IncludeYtDlp -and -not $ExcludeYtDlp
$canonicalSettingsName = "smart_sentry_v${activeVersionToken}_settings.json"
$canonicalPresetsName = "smart_sentry_v${activeVersionToken}_custom_presets.json"
$canonicalPromptedTargetsName = "smart_sentry_v${activeVersionToken}_prompted_targets.json"
$canonicalFacesName = "smart_sentry_v${activeVersionToken}_faces.json"
$canonicalSettingsRelativePath = "app/config/$canonicalSettingsName"
$canonicalPromptedTargetsRelativePath = "app/config/$canonicalPromptedTargetsName"
$canonicalFacesRelativePath = "app/config/$canonicalFacesName"
$canonicalUdpHost = '192.168.4.1'
$canonicalUdpPort = 9000

if (-not (Test-DriveRootAvailable $OutputDrive)) {
    throw "Compilation protocol requires output on $OutputDrive, but that drive is not available."
}

if ($Clean) {
    if (Test-Path $legacyBuildRoot) {
        Remove-Item $legacyBuildRoot -Recurse -Force -ErrorAction SilentlyContinue
    }
    if (Test-Path $releaseDir) {
        Remove-DirectoryRobust $releaseDir
    }
    foreach ($path in @($distRoot, $workRoot, $specRoot)) {
        if (Test-Path $path) {
            Remove-Item $path -Recurse -Force -ErrorAction SilentlyContinue
        }
    }
}

foreach ($path in @($distRoot, $workRoot, $specRoot)) {
    if (Test-Path $path) {
        Remove-Item $path -Recurse -Force -ErrorAction SilentlyContinue
    }
    New-Item -ItemType Directory -Force -Path $path | Out-Null
}

$runScriptPath = Join-Path $repoRoot 'run.py'
$packagingPreflightPath = Join-Path $repoRoot 'tools\validate_packaging_entrypoints.py'
$iconPath = Join-Path $repoRoot 'smart_sentry_icon.ico'
$appConfigPath = Join-Path $repoRoot 'app\config'
$appSentryConfigPath = Join-Path $repoRoot 'app\sentry_v2\config'
$appLogoPath = Join-Path $repoRoot 'app\LOGO.png'
$recentUpdatesPath = Join-Path $repoRoot 'RECENT_UPDATES.json'
$releaseVersionPath = $activeVersionMetadata.MarkerPath
$db3kVersionPath = Join-Path $repoRoot 'DB3K_VERSION.txt'
$rootModelsPath = Join-Path $repoRoot 'YOLO_MODELS'

if (-not (Test-Path $activeLauncherPath)) {
    throw "App launcher was not found: $activeLauncherPath"
}

$requiredModules = @('PyInstaller', 'PyQt5', 'cv2', 'numpy', 'serial', 'torch', 'ultralytics', 'lap')
if ($bundleSklearn) {
    $requiredModules += 'sklearn'
}
if ($bundleYtDlp) {
    $requiredModules += 'yt_dlp'
}

Assert-PythonModulesAvailable -pythonCommand $pythonExe -moduleNames $requiredModules

if ($bundleModels) {
    if (-not (Test-Path $rootModelsPath)) {
        throw "Full portable build requires a local YOLO_MODELS folder, but it was not found: $rootModelsPath"
    }
    $bundledModelFiles = @(Get-ChildItem $rootModelsPath -File -Recurse | Where-Object { $_.Extension.ToLowerInvariant() -in @('.pt', '.onnx', '.engine', '.torchscript') })
    if ($bundledModelFiles.Count -eq 0) {
        throw "Full portable build requires at least one YOLO model file in $rootModelsPath"
    }
}

& $pythonExe $packagingPreflightPath
if ($LASTEXITCODE -ne 0) {
    throw 'Packaging preflight failed. Resolve missing launcher/module imports before packaging.'
}

$pyInstallerHooksDir = Join-Path $repoRoot 'pyinstaller_hooks'

$pyInstallerArgs = @(
    '-m', 'PyInstaller',
    '--noconfirm',
    '--clean',
    '--onedir',
    '--windowed',
    '--name', $releaseExeBase,
    '--contents-directory', $releaseContentsDirName,
    '--icon', $iconPath,
    '--additional-hooks-dir', $pyInstallerHooksDir,
    '--paths', $repoRoot,
    '--paths', (Join-Path $repoRoot 'app'),
    '--distpath', $distRoot,
    '--workpath', $workRoot,
    '--specpath', $specRoot,
    '--collect-all', 'torchvision',
    '--collect-all', 'ultralytics',
    '--exclude-module', 'onnxscript',
    '--exclude-module', 'onnxscript.onnx_opset',
    '--exclude-module', 'onnx_ir',
    '--exclude-module', 'onnx.reference',
    '--exclude-module', 'onnx.reference.ops',
    '--exclude-module', 'onnx.reference.op_run',
    '--exclude-module', 'onnx.reference.custom_element_types',
    '--exclude-module', 'polars',
    '--exclude-module', 'polars_runtime_32',
    '--exclude-module', '_polars_runtime_32',
    '--exclude-module', 'pytest',
    '--hidden-import', 'app.main',
    '--hidden-import', 'app.runtime_paths',
    '--hidden-import', 'smart_sentry_meta',
    '--hidden-import', 'theme_manager',
    '--hidden-import', 'torch',
    '--hidden-import', 'torchvision',
    '--hidden-import', 'sentry_v2.sentry_v2_tab',
    '--add-data', "$appConfigPath;app/config",
    '--add-data', "$appSentryConfigPath;app/sentry_v2/config",
    '--add-data', "$appLogoPath;app",
    '--add-data', "$recentUpdatesPath;.",
    '--add-data', "$releaseVersionPath;.",
    '--add-data', "$db3kVersionPath;.",
    $runScriptPath
)

$torchRuntimeExcludes = @(
    'torch.testing',
    'torch.testing._internal',
    'torch.distributed._shard',
    'torch.distributed._sharded_tensor',
    'torch.distributed._sharding_spec',
    'torch.onnx._internal.exporter._testing',
    'torch.onnx.testing',
    'torch.onnx.verification',
    'torch.utils.benchmark'
)

foreach ($excludedTorchModule in $torchRuntimeExcludes) {
    $pyInstallerArgs += @('--exclude-module', $excludedTorchModule)
}


if (-not $bundleSklearn) {
    $pyInstallerArgs += @(
        '--exclude-module', 'sklearn',
        '--exclude-module', 'matplotlib',
        '--exclude-module', 'matplotlib.tests'
    )
}
if (-not $bundleYtDlp) {
    $pyInstallerArgs += @('--exclude-module', 'yt_dlp')
}

if ($bundleSklearn) {
    $pyInstallerArgs += @(
        '--collect-data', 'sklearn',
        '--collect-binaries', 'sklearn',
        '--collect-submodules', 'sklearn.neural_network',
        '--hidden-import', 'sklearn',
        '--hidden-import', 'sklearn.neural_network',
        '--hidden-import', 'sklearn.neural_network._multilayer_perceptron'
    )
}

if ($cv2DataPath -and (Test-Path $cv2DataPath)) {
    $pyInstallerArgs += @('--add-data', "$cv2DataPath;cv2/data")
}
if ($bundleYtDlp) {
    $pyInstallerArgs += @('--collect-all', 'yt_dlp')
}
if ($bundleModels -and (Test-Path $rootModelsPath)) {
    $pyInstallerArgs += @('--add-data', "$rootModelsPath;YOLO_MODELS")
}

$pyInstallerExitCode = Invoke-NativeProcess -filePath $pythonExe -arguments $pyInstallerArgs -workingDirectory $repoRoot
if ($pyInstallerExitCode -ne 0) {
    exit $pyInstallerExitCode
}

$outputDir = $stagingDir
if (-not (Test-Path $outputDir)) {
    throw "PyInstaller build output directory was not found: $outputDir"
}

$releaseContentsDir = Join-Path $outputDir $releaseContentsDirName
if (-not (Test-Path $releaseContentsDir)) {
    throw "Expected versioned support folder was not created: $releaseContentsDir"
}

Assert-RequiredReleaseArtifacts -buildRoot $outputDir -exeName $releaseExeName -contentsDirName $releaseContentsDirName -pythonRuntimeDllName $pythonRuntimeDllName

$yoloDir = Join-Path $releaseContentsDir 'YOLO_MODELS'
$publicYoloDir = Join-Path $outputDir 'YOLO_MODELS'

New-Item -ItemType Directory -Force -Path $publicYoloDir | Out-Null

$publicReadmePath = Join-Path $publicYoloDir 'README.txt'
@(
    'Add extra YOLO model files here after the build completes.',
    'Supported formats: .pt, .onnx, .engine, .torchscript',
    'This is the public release model drop folder beside the packaged executable.',
    'Bundled default models remain under the versioned support folder.'
) | Set-Content -Path $publicReadmePath -Encoding ASCII

New-Item -ItemType Directory -Force -Path $yoloDir | Out-Null

if ($bundleModels) {
    Copy-Item -Path (Join-Path $rootModelsPath '*') -Destination $yoloDir -Recurse -Force
    Copy-Item -Path (Join-Path $rootModelsPath '*') -Destination $publicYoloDir -Recurse -Force
    Set-PackagedConfigSurface -configPath (Join-Path $releaseContentsDir "app\config\$canonicalSettingsName") -settingsRelativePath $canonicalSettingsRelativePath -promptedRelativePath $canonicalPromptedTargetsRelativePath -faceRelativePath $canonicalFacesRelativePath -modelDir $publicYoloDir -udpHost $canonicalUdpHost -udpPort $canonicalUdpPort
} else {
    New-Item -ItemType Directory -Force -Path $yoloDir | Out-Null

    $readmePath = Join-Path $yoloDir 'README.txt'
    @(
        'Bundled/default YOLO models live in this support folder.',
        'Add extra operator-supplied models to the release-root YOLO_MODELS folder beside the executable.'
    ) | Set-Content -Path $readmePath -Encoding ASCII
}

$releaseExePath = Join-Path $outputDir $releaseExeName
if (-not (Test-Path $releaseExePath)) {
    throw "Expected release executable was not created: $releaseExePath"
}

$smokeProcess = Start-Process -FilePath $releaseExePath -PassThru
try {
    Wait-Process -Id $smokeProcess.Id -Timeout 5 -ErrorAction SilentlyContinue
    if ($smokeProcess.HasExited) {
        throw "Packaged executable exited during smoke test with code $($smokeProcess.ExitCode): $releaseExePath"
    }
} finally {
    if ($smokeProcess -and -not $smokeProcess.HasExited) {
        Stop-Process -Id $smokeProcess.Id -Force -ErrorAction SilentlyContinue
    }
}

New-Item -ItemType Directory -Force -Path $releaseDir | Out-Null
Get-ChildItem $releaseDir -Force -ErrorAction SilentlyContinue | ForEach-Object {
    Remove-DirectoryRobust $_.FullName
}
Copy-Item -Path (Join-Path $outputDir '*') -Destination $releaseDir -Recurse -Force
Sync-QtVcRuntimeDlls -releaseRoot $releaseDir -contentsDirName $releaseContentsDirName

$releaseExePath = Join-Path $releaseDir $releaseExeName
Assert-RequiredReleaseArtifacts -buildRoot $releaseDir -exeName $releaseExeName -contentsDirName $releaseContentsDirName -pythonRuntimeDllName $pythonRuntimeDllName
Patch-BundledUltralyticsGit -contentsDirPath (Join-Path $releaseDir $releaseContentsDirName)

if ($bundleModels) {
    Set-PackagedConfigSurface -configPath (Join-Path $releaseDir "$releaseContentsDirName\app\config\$canonicalSettingsName") -settingsRelativePath $canonicalSettingsRelativePath -promptedRelativePath $canonicalPromptedTargetsRelativePath -faceRelativePath $canonicalFacesRelativePath -modelDir (Join-Path $releaseDir 'YOLO_MODELS') -udpHost $canonicalUdpHost -udpPort $canonicalUdpPort
}

foreach ($path in @($distRoot, $workRoot, $specRoot, $legacyBuildRoot)) {
    if (Test-Path $path) {
        Remove-Item $path -Recurse -Force -ErrorAction SilentlyContinue
    }
}

$releaseSupportDirPath = Join-Path $releaseDir $releaseContentsDirName
$releaseModelDropDir = Join-Path $releaseSupportDirPath 'YOLO_MODELS'
$releasePublicModelDropDir = Join-Path $releaseDir 'YOLO_MODELS'

Write-Host "Protocol-aligned release folder: $releaseDir"
Write-Host "Protocol-aligned release executable: $releaseExePath"
Write-Host "Versioned support folder: $releaseSupportDirPath"
Write-Host "Public release model drop folder: $releasePublicModelDropDir"
if (-not $bundleModels) {
    Write-Host 'Models were excluded from the build for a reduced package footprint.'
    Write-Host "Bundled/default support-model folder: $releaseModelDropDir"
} else {
    Write-Host 'Full-release model bundling is enabled. Root and support-folder YOLO model directories were populated automatically.'
}
if (-not $bundleSklearn) {
    Write-Host 'scikit-learn was excluded. ML threat refinement remains unavailable unless you rebuild without -ExcludeSklearn.'
}
if (-not $bundleYtDlp) {
    Write-Host 'yt-dlp was excluded. YouTube URL playback will be unavailable unless you rebuild without -ExcludeYtDlp.'
}