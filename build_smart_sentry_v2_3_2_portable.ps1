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

function Assert-RequiredReleaseArtifacts([string]$buildRoot, [string]$exeName, [string]$contentsDirName, [string]$pythonRuntimeDllName) {
    $contentsDirPath = Join-Path $buildRoot $contentsDirName
    $requiredPaths = @(
        (Join-Path $buildRoot $exeName),
        $contentsDirPath,
        (Join-Path $contentsDirPath 'base_library.zip'),
        (Join-Path $contentsDirPath 'python3.dll'),
        (Join-Path $contentsDirPath $pythonRuntimeDllName)
    )

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
$activeLauncherBaseName = "run_smart_sentry_v$activeVersionToken"
$activeLauncherModule = "app.$activeLauncherBaseName"
$activeLauncherPath = Join-Path $repoRoot "app\$activeLauncherBaseName.py"
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

$pythonRuntimeDllName = (& $pythonExe -c "import sys; print(f'python{sys.version_info.major}{sys.version_info.minor}.dll')").Trim()
if (-not $pythonRuntimeDllName) {
    throw 'Unable to determine the Python runtime DLL name for the selected interpreter.'
}

$bundleModels = -not $ExcludeModels
$bundleSklearn = $IncludeSklearn -and -not $ExcludeSklearn
$bundleYtDlp = $IncludeYtDlp -and -not $ExcludeYtDlp
$canonicalSettingsName = "smart_sentry_v${activeVersionToken}_settings.json"
$canonicalPresetsName = "smart_sentry_v${activeVersionToken}_custom_presets.json"
$canonicalPromptedTargetsName = "smart_sentry_v${activeVersionToken}_prompted_targets.json"
$legacyV3SettingsName = 'smart_sentry_v3_settings.json'
$legacyV3PresetsName = 'smart_sentry_v3_custom_presets.json'
$legacyV3PromptedTargetsName = 'smart_sentry_v3_prompted_targets.json'
$legacyV2SettingsName = 'sentry_v2_settings.json'
$legacyV2PresetsName = 'sentry_v2_custom_presets.json'
$legacyV2PromptedTargetsName = 'sentry_v2_prompted_targets.json'

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
    throw "Active launcher for version $activeVersion was not found: $activeLauncherPath"
}

$requiredModules = @('PyInstaller', 'PyQt5', 'cv2', 'numpy', 'serial', 'torch', 'ultralytics')
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

$pyInstallerArgs = @(
    '-m', 'PyInstaller',
    '--noconfirm',
    '--clean',
    '--onedir',
    '--windowed',
    '--name', $releaseExeBase,
    '--contents-directory', $releaseContentsDirName,
    '--icon', $iconPath,
    '--paths', $repoRoot,
    '--paths', (Join-Path $repoRoot 'app'),
    '--distpath', $distRoot,
    '--workpath', $workRoot,
    '--specpath', $specRoot,
    '--collect-all', 'torch',
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
    '--hidden-import', $activeLauncherModule,
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

$stagingConfigDir = Join-Path $releaseContentsDir 'app\config'
Copy-ReleaseConfigAlias -sourcePath (Join-Path $stagingConfigDir $legacyV3SettingsName) -targetPath (Join-Path $stagingConfigDir $canonicalSettingsName)
Copy-ReleaseConfigAlias -sourcePath (Join-Path $stagingConfigDir $legacyV3PresetsName) -targetPath (Join-Path $stagingConfigDir $canonicalPresetsName)
Copy-ReleaseConfigAlias -sourcePath (Join-Path $stagingConfigDir $legacyV3PromptedTargetsName) -targetPath (Join-Path $stagingConfigDir $canonicalPromptedTargetsName)
Copy-ReleaseConfigAlias -sourcePath (Join-Path $stagingConfigDir $legacyV2SettingsName) -targetPath (Join-Path $stagingConfigDir $canonicalSettingsName)
Copy-ReleaseConfigAlias -sourcePath (Join-Path $stagingConfigDir $legacyV2PresetsName) -targetPath (Join-Path $stagingConfigDir $canonicalPresetsName)
Copy-ReleaseConfigAlias -sourcePath (Join-Path $stagingConfigDir $legacyV2PromptedTargetsName) -targetPath (Join-Path $stagingConfigDir $canonicalPromptedTargetsName)

Remove-ReleaseConfigAlias -targetPath (Join-Path $stagingConfigDir $legacyV3SettingsName)
Remove-ReleaseConfigAlias -targetPath (Join-Path $stagingConfigDir $legacyV3PresetsName)
Remove-ReleaseConfigAlias -targetPath (Join-Path $stagingConfigDir $legacyV3PromptedTargetsName)
Remove-ReleaseConfigAlias -targetPath (Join-Path $stagingConfigDir $legacyV2SettingsName)
Remove-ReleaseConfigAlias -targetPath (Join-Path $stagingConfigDir $legacyV2PresetsName)
Remove-ReleaseConfigAlias -targetPath (Join-Path $stagingConfigDir $legacyV2PromptedTargetsName)

if ($bundleModels) {
    Copy-Item -Path (Join-Path $rootModelsPath '*') -Destination $yoloDir -Recurse -Force
    Copy-Item -Path (Join-Path $rootModelsPath '*') -Destination $publicYoloDir -Recurse -Force
    Set-PackagedYoloConfig -configPath (Join-Path $releaseContentsDir "app\config\$canonicalSettingsName") -modelDir $publicYoloDir
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

$releaseExePath = Join-Path $releaseDir $releaseExeName
Assert-RequiredReleaseArtifacts -buildRoot $releaseDir -exeName $releaseExeName -contentsDirName $releaseContentsDirName -pythonRuntimeDllName $pythonRuntimeDllName

if ($bundleModels) {
    Set-PackagedYoloConfig -configPath (Join-Path $releaseDir "$releaseContentsDirName\app\config\$canonicalSettingsName") -modelDir (Join-Path $releaseDir 'YOLO_MODELS')
}

$releaseConfigDir = Join-Path $releaseDir "$releaseContentsDirName\app\config"
Remove-ReleaseConfigAlias -targetPath (Join-Path $releaseConfigDir $legacyV3SettingsName)
Remove-ReleaseConfigAlias -targetPath (Join-Path $releaseConfigDir $legacyV3PresetsName)
Remove-ReleaseConfigAlias -targetPath (Join-Path $releaseConfigDir $legacyV3PromptedTargetsName)
Remove-ReleaseConfigAlias -targetPath (Join-Path $releaseConfigDir $legacyV2SettingsName)
Remove-ReleaseConfigAlias -targetPath (Join-Path $releaseConfigDir $legacyV2PresetsName)
Remove-ReleaseConfigAlias -targetPath (Join-Path $releaseConfigDir $legacyV2PromptedTargetsName)

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