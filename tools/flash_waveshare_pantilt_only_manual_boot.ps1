param(
    [string]$Port = "COM30",
    [string]$Fqbn = "esp32:esp32:esp32"
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$cliPath = Join-Path $PSScriptRoot "arduino-cli\arduino-cli.exe"
$pythonExe = Join-Path (Split-Path -Parent $repoRoot) ".venv\Scripts\python.exe"
$sketchDir = Join-Path $repoRoot "arduino\SMART_SENTRY_V3_0_WAVESHARE_WIFI_PANTILT_ONLY"
$buildDir = Join-Path $repoRoot "logs\precision_tuning\waveshare_pantilt_only_build_manual"

if (-not (Test-Path $cliPath)) {
    throw "Arduino CLI not found at $cliPath"
}

if (-not (Test-Path $pythonExe)) {
    throw "Python executable not found at $pythonExe"
}

if (-not (Test-Path $sketchDir)) {
    throw "Sketch directory not found at $sketchDir"
}

New-Item -ItemType Directory -Force -Path $buildDir | Out-Null

Write-Host "[MANUAL-FLASH] Compiling Waveshare pan/tilt-only sketch"
& $cliPath compile --fqbn $Fqbn --build-path $buildDir $sketchDir
if ($LASTEXITCODE -ne 0) {
    throw "Compile failed"
}

$bootloader = Join-Path $buildDir "SMART_SENTRY_V3_0_WAVESHARE_WIFI_PANTILT_ONLY.ino.bootloader.bin"
$partitions = Join-Path $buildDir "SMART_SENTRY_V3_0_WAVESHARE_WIFI_PANTILT_ONLY.ino.partitions.bin"
$appBin = Join-Path $buildDir "SMART_SENTRY_V3_0_WAVESHARE_WIFI_PANTILT_ONLY.ino.bin"

foreach ($path in @($bootloader, $partitions, $appBin)) {
    if (-not (Test-Path $path)) {
        throw "Expected build artifact not found: $path"
    }
}

Write-Host "[MANUAL-FLASH] Put the Waveshare UART control switch in the ESP32 position."
Write-Host "[MANUAL-FLASH] Hold BOOT, tap RESET, then release BOOT once the board is in download mode."
Read-Host "[MANUAL-FLASH] Press Enter when the board is ready to flash on $Port"

Write-Host "[MANUAL-FLASH] Flashing pan/tilt-only sketch to $Port"
& $pythonExe -m esptool --chip esp32 --port $Port --baud 115200 write-flash -z `
    0x1000 $bootloader `
    0x8000 $partitions `
    0x10000 $appBin

if ($LASTEXITCODE -ne 0) {
    throw "Flash failed"
}

Write-Host "[MANUAL-FLASH] Flash complete"