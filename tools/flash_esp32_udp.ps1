param(
    [Parameter(Mandatory = $true)]
    [string]$Port,

    [Parameter(Mandatory = $true)]
    [string]$Sketch,

    [string]$Fqbn = "esp32:esp32:esp32",

    [switch]$BuildOnly,

    [switch]$InstallCore,

    [switch]$CliVerbose
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$cliPath = Join-Path $PSScriptRoot "arduino-cli\arduino-cli.exe"

if (-not (Test-Path $cliPath)) {
    throw "Arduino CLI not found at $cliPath"
}

$sketchPath = Join-Path $repoRoot $Sketch
if (-not (Test-Path $sketchPath)) {
    throw "Sketch path not found: $sketchPath"
}

$sketchTarget = $sketchPath
if ([System.IO.Path]::GetExtension($sketchPath).Equals('.ino', [System.StringComparison]::OrdinalIgnoreCase)) {
    $sketchTarget = Split-Path -Parent $sketchPath
}

if ($InstallCore) {
    & $cliPath core install "esp32:esp32"
}

$compileArgs = @("compile", "--fqbn", $Fqbn)
if ($CliVerbose) {
    $compileArgs += "--verbose"
}
$compileArgs += $sketchTarget

Write-Host "[FLASH] Compiling $Sketch for $Fqbn"
& $cliPath @compileArgs
if ($LASTEXITCODE -ne 0) {
    throw "Compile failed"
}

if ($BuildOnly) {
    Write-Host "[FLASH] Build-only mode complete"
    exit 0
}

$uploadArgs = @("upload", "-p", $Port, "--fqbn", $Fqbn)
if ($CliVerbose) {
    $uploadArgs += "--verbose"
}
$uploadArgs += $sketchTarget

Write-Host "[FLASH] Uploading $Sketch to $Port"
& $cliPath @uploadArgs
if ($LASTEXITCODE -ne 0) {
    throw "Upload failed"
}

Write-Host "[FLASH] Upload complete"