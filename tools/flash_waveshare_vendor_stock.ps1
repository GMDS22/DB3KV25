param(
    [string]$Port = "COM30",
    [switch]$SkipPrompt
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$workspaceRoot = Split-Path -Parent $repoRoot
$pythonExe = Join-Path $workspaceRoot ".venv\Scripts\python.exe"
$vendorRoot = Join-Path $workspaceRoot "Waveshare_Bus_Servo_Driver_HAT_A_Vendor"
$binRoot = Join-Path $vendorRoot "bin"

if (-not (Test-Path $pythonExe)) {
    throw "Python executable not found at $pythonExe"
}

if (-not (Test-Path $binRoot)) {
    throw "Vendor bin folder not found at $binRoot"
}

$bootloader = Join-Path $binRoot "bootloader_dio_40m.bin"
$partitions = Join-Path $binRoot "default.bin"
$bootApp = Join-Path $binRoot "boot_app0.bin"
$appBin = Join-Path $binRoot "ServoDriverST.ino.bin"

foreach ($path in @($bootloader, $partitions, $bootApp, $appBin)) {
    if (-not (Test-Path $path)) {
        throw "Required vendor image not found: $path"
    }
}

Write-Host "[VENDOR-FLASH] Using stock Waveshare ESP32 bundle on $Port"
Write-Host "[VENDOR-FLASH] bootloader=$bootloader"
Write-Host "[VENDOR-FLASH] partitions=$partitions"
Write-Host "[VENDOR-FLASH] boot_app0=$bootApp"
Write-Host "[VENDOR-FLASH] app=$appBin"

if (-not $SkipPrompt) {
    Write-Host "[VENDOR-FLASH] Put the Waveshare UART control switch in the ESP32 position."
    Write-Host "[VENDOR-FLASH] If auto-reset fails, hold BOOT, tap RESET, then release BOOT once download mode is entered."
    Read-Host "[VENDOR-FLASH] Press Enter when ready to flash on $Port"
}

& $pythonExe -m esptool --chip esp32 --port $Port --baud 115200 write-flash -z `
    0x1000 $bootloader `
    0x8000 $partitions `
    0xe000 $bootApp `
    0x10000 $appBin

if ($LASTEXITCODE -ne 0) {
    throw "Vendor flash failed"
}

Write-Host "[VENDOR-FLASH] Flash complete"