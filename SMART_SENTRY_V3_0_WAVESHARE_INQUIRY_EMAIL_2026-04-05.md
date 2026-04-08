Subject: Inquiry on Waveshare single-board Smart Sentry v3 bridge issue

Hello,

I am writing to summarize the issue we encountered while trying to use the Waveshare ESP32 board as a single-board WiFi bridge for Smart Sentry v3 pan/tilt motion and accessories.

We completed staged firmware reintroduction, direct UDP probing, app-path verification, and several UART handling revisions. The stable WiFi point was Step 7 A3, and direct bench tests confirmed that the board could answer valid UDP traffic on `192.168.4.1:9000`. We also found and corrected an app-side configuration issue where movement was being sent in dual-ESP32 mode instead of the correct single-board mode.

After that fix, we tested newer non-blocking UART state-machine builds. Step 7.6 remained network-stable, but it could not prove motion because servo writes are only compiled at Step 9 and above. A Step 9 motion-capable build was then flashed, but no visible servo movement was observed, and the motion-capable network path became unstable during direct validation. We also identified that the staged sketch was still using `250000` baud while the vendor-aligned bridge path uses `1000000`, so a `1000000` baud follow-up build was compiled, but testing was stopped before hardware validation.

Based on the results, the final practical solution is to stop using the Waveshare board as the single-board WiFi motion bridge. The approved fallback is to use the Debug Board over USB for pan/tilt motion and keep the Waveshare ESP32 on WiFi for IO and accessory control only.

Regards,

Smart Sentry v3 test bench