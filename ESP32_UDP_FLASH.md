# ESP32 UDP Link Flash Workflow

This guide flashes the ESP32 UDP link firmware using the included Arduino CLI.

## Prereqs
- Board: ESP32 DevKit v1 (WROOM-32)
- Arduino CLI: tools/arduino-cli/arduino-cli.exe (already in repo)
- ESP32 core installed (see setup below)

## ESP32 Core Setup (one-time)
Use the ESP32 board manager URL:
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

Option A (Arduino IDE):
1) File -> Preferences -> Additional Boards Manager URLs
2) Add the URL above
3) Tools -> Board -> Boards Manager -> install "esp32"

Option B (Arduino CLI):
1) arduino-cli config init
2) arduino-cli config set board_manager.additional_urls https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
3) arduino-cli core update-index
4) arduino-cli core install esp32:esp32

## Flash (PowerShell)
From repo root:

```powershell
# list ports
.\tools\arduino-cli\arduino-cli.exe board list

# upload
.\tools\flash_esp32_udp.ps1 -Port COM5
```

Add -InstallCore if you want the script to attempt core install:

```powershell
.\tools\flash_esp32_udp.ps1 -Port COM5 -InstallCore
```

## Sketch Location
- arduino/DB3000_ESP32_UDP_Link/DB3000_ESP32_UDP_Link.ino

## Defaults
- WiFi AP SSID: DB3000-ESP32
- WiFi AP password: db3000pass
- UDP port: 9000
