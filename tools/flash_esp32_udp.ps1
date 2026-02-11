param(
    [string]$Port,
    [string]$Sketch = "arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino",
    [string]$Fqbn = "esp32:esp32:esp32",
    [switch]$InstallCore
)

$RepoRoot = Split-Path -Parent $PSScriptRoot
$Cli = Join-Path $RepoRoot "tools/arduino-cli/arduino-cli.exe"
$SketchPath = Join-Path $RepoRoot $Sketch

if (-not (Test-Path $Cli)) {
    Write-Error "arduino-cli.exe not found at $Cli"
    exit 1
}

if (-not (Test-Path $SketchPath)) {
    Write-Error "Sketch not found at $SketchPath"
    exit 1
}

if ($InstallCore) {
    & $Cli core update-index
    if ($LASTEXITCODE -ne 0) {
        Write-Error "core update-index failed. Ensure ESP32 board manager URL is configured."
        exit 1
    }
    & $Cli core install esp32:esp32
    if ($LASTEXITCODE -ne 0) {
        Write-Error "core install esp32:esp32 failed. Ensure ESP32 board manager URL is configured."
        exit 1
    }
}

if (-not $Port) {
    & $Cli board list
    Write-Error "Missing -Port. Example: .\tools\flash_esp32_udp.ps1 -Port COM5"
    exit 1
}

& $Cli compile --fqbn $Fqbn $SketchPath
if ($LASTEXITCODE -ne 0) {
    Write-Error "Compile failed"
    exit 1
}

& $Cli upload --fqbn $Fqbn --port $Port $SketchPath
if ($LASTEXITCODE -ne 0) {
    Write-Error "Upload failed"
    exit 1
}

Write-Host "Upload complete."
