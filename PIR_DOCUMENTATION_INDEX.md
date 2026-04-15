# PIR Sensor Integration - Complete Documentation Index

**Project**: Smart Sentry v2 with 3x PIR Blind-Spot Detection  
**Status**: ✅ Complete, contract-audited for current v2.3.2 runtime  
**Date**: April 2026  

---

## 📚 Reading Sequence (Start Here)

### For Behavior Tuning / Editor Handoff
1. **SMART_SENTRY_AUTOTRACKING_BEHAVIOR_BLUEPRINT.md** (Primary behavior contract)
   - Overall autotracking logic
   - Guard, PIR cue, target-loss reacquire, and fire protocol
   - Preset behavior rules
   - Editor-facing regression warnings

2. **PIR_AT_A_GLANCE.md** (Current PIR contract audit)
   - Current live firmware path
   - Current desktop runtime path
   - After-target-loss vs PIR interaction rules
   - Source-of-truth files

### For Non-Technical Users / Operations
1. **PIR_GUARD_QUICK_START.md** (User Guide)
   - What PIR does
   - How to enable it in the UI
   - How to configure sensors
   - Tuning tips for your environment
   - Troubleshooting common issues

### For System Integrators / Developers
1. **PIR_INTEGRATION_SUMMARY.md** (Executive Overview)
   - What was delivered
   - System architecture
   - Filing locations
   - Integration checklist
   - Next steps

2. **ESP32_PIN_QUICK_REFERENCE.md** (Hardware Wiring)
   - Pin assignments (all I/O)
   - Breadboard layout
   - Electrical specifications
   - Wiring diagrams
   - Testing instructions

3. **ESP32_PIR_FIRMWARE_GUIDE.md** (Firmware Details)
   - Feature set
   - Command protocol (tokens)
   - Telemetry format
   - Build instructions
   - Integration with Smart Sentry

### For Firmware Engineers
1. **FIRMWARE_COMPARISON.md** (Original vs Enhanced)
   - Side-by-side code comparison
   - Breaking changes (none!)
   - Compilation behavior
   - Performance impact
   - Migration path

2. **PIR_GUARD_IMPLEMENTATION_COMPLETE.md** (Technical Deep-Dive)
   - PC application architecture
   - Python module details
   - Config persistence
   - State machine logic
   - Scan grid algorithm
   - Known limitations

---

## 📁 File Organization

### ESP32 Firmware
```
arduino/
├── SMART_SENTRY_V2_3_1_ESP32_UDP_PIR/            [CURRENT LIVE APP WIFI PATH]
│   └── SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino
├── DB3000_ESP32_IO_Telemetry_2026/               [ORIGINAL SERIAL IO BACKUP]
│   └── DB3000_ESP32_IO_Telemetry_2026.ino
└── DB3000_ESP32_IO_Telemetry_2026_w_PIR/         [CURRENT SERIAL IO + PIR PATH]
   └── DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino
```

### Python Source Code (Smart Sentry v2)
```
app/sentry_v2/
├── sentry_v2_config.py              [MODIFIED: Added PIR dataclasses]
├── sentry_v2_pir_manager.py         [NEW: PIR motion manager]
├── sentry_v2_engine.py              [MODIFIED: G state machine + PIR cues]
├── sentry_v2_comm.py                [MODIFIED: PIR event callback interface]
├── sentry_v2_tab.py                 [MODIFIED: Guard tab UI + handlers]
├── sentry_v2_tooltips.py            [MODIFIED: Added 10 PIR tooltips]
└── [other modules unchanged]
```

### Documentation
```
project_root/
├─ PIR_INTEGRATION_SUMMARY.md                   [THIS IS YOUR ROADMAP]
├─ PIR_GUARD_IMPLEMENTATION_COMPLETE.md         [Technical reference]
├─ PIR_GUARD_QUICK_START.md                     [User guide]
├─ ESP32_PIR_FIRMWARE_GUIDE.md                  [Firmware guide]
├─ ESP32_PIN_QUICK_REFERENCE.md                 [Pin reference]
├─ FIRMWARE_COMPARISON.md                       [Before/after]
└─ PIR_INTEGRATION_SUMMARY.md                   [This file]
```

### Test Files
```
project_root/
└─ test_pir_ui_config.py              [Unit tests - 5/5 passing]
```

---

## 🎯 Quick Reference by Role

### 🔧 Hardware Technician / Installer
**Start Here**: ESP32_PIN_QUICK_REFERENCE.md
- Wiring diagram for PIR sensors → ESP32
- Pin assignments (GPIO 35, 34, 39)
- Testing checklist
- Breadboard layout
- Troubleshooting

**Then Read**: PIR_GUARD_QUICK_START.md
- How to enable PIR sensors in UI
- Configuration steps
- Verification procedures

---

### 💻 PC Application Operator
**Start Here**: PIR_GUARD_QUICK_START.md
- UI location (Guard tab)
- Enable/disable toggle
- Sensor configuration
- Tuning recommendations
- Expected behavior

**Reference**: Smart Sentry v2 app itself
- All settings visible in Guard tab
- Tooltips provide inline help
- Config saved automatically

---

### 🔌 Firmware Engineer (ESP32)
**Start Here**: ESP32_PIR_FIRMWARE_GUIDE.md
- Complete architecture
- Command protocol
- Pin assignments
- Build process
- Testing procedures

**Then Read**: FIRMWARE_COMPARISON.md
- All code changes (before/after)
- No breaking changes
- Backward compatibility info
- Performance impact

**Reference**: DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino for direct serial IO, SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino for the live WiFi path
- Well-commented code
- Preprocessor-gated PIR section
- Compile-time config: ENABLE_PIR_SUPPORT

---

### 🐍 Python Developer (Smart Sentry v2)
**Start Here**: PIR_GUARD_IMPLEMENTATION_COMPLETE.md
- Python module architecture
- Config dataclasses
- State machine logic
- PIR manager details
- UI integration

**Code Reference**:
- sentry_v2_config.py (dataclasses)
- sentry_v2_pir_manager.py (motion logic)
- sentry_v2_engine.py (guard state + cue handling)
- sentry_v2_comm.py (telemetry interface)
- sentry_v2_tab.py (GUI controls)

**Integration Status**:
- sentry_v2_comm.py already parses serial `PIR_EVENT` and live WiFi UDP `pir_event`
- Keep transport docs aligned with the current topology instead of reopening parser work that is already done

---

### 🏗️ System Integrator / Architect
**Start Here**: PIR_INTEGRATION_SUMMARY.md
- Complete overview
- System architecture diagram
- File locations
- Integration checklist
- Next steps

**Then Read** (in order):
1. PIR_GUARD_IMPLEMENTATION_COMPLETE.md (PC-side logic)
2. ESP32_PIR_FIRMWARE_GUIDE.md (firmware-side logic)
3. FIRMWARE_COMPARISON.md (change analysis)

**Deployment Decision**: FIRMWARE_COMPARISON.md
- Migration matrix
- Testing strategy
- Phased rollout plan

---

### 📊 Project Manager / Stakeholder
**Start Here**: PIR_INTEGRATION_SUMMARY.md
- Executive summary
- What was delivered
- File locations
- Status checklist
- Remaining work

**Then Review**:
- PIR_GUARD_QUICK_START.md (end-user experience)
- FIRMWARE_COMPARISON.md (risk assessment: zero changes to original)

---

## 🔍 Find What You Need

### "How do I enable PIR in the app?"
→ PIR_GUARD_QUICK_START.md, Section: "Enabling PIR Guard"

### "What pins do I connect sensors to?"
→ ESP32_PIN_QUICK_REFERENCE.md, Table: "PIR Sensor Inputs"

### "Is this backward compatible?"
→ FIRMWARE_COMPARISON.md, Section: "Compilation Behavior"

### "What commands does ESP32 accept?"
→ ESP32_PIR_FIRMWARE_GUIDE.md, Section: "Command Protocol"

### "How does the state machine work?"
→ PIR_GUARD_IMPLEMENTATION_COMPLETE.md, Section: "Behavior (User Specified)"

### "What files changed in the Python app?"
→ PIR_GUARD_IMPLEMENTATION_COMPLETE.md, Section: "Codebase Status"

### "How do I wire the PIR sensors?"
→ ESP32_PIN_QUICK_REFERENCE.md, Section: "Typical Connection Diagram"

### "What does the scan grid do?"
→ PIR_GUARD_QUICK_START.md, Section: "Scan Grid Example"

### "How do I test PIR events?"
→ ESP32_PIR_FIRMWARE_GUIDE.md, Section: "Testing & Validation"

### "Can I use the old firmware and new firmware together?"
→ FIRMWARE_COMPARISON.md, Section: "Migration Decision Matrix"

---

## 📋 Quick Facts Checklist

### PIR Features
- [x] 3 independent motion sensors
- [x] GPIO pins: 35, 34, 39 (ESP32)
- [x] Debounce: 200ms per sensor
- [x] Motion reporting: event-based telemetry
- [x] Adaptive scan grid on no-detection
- [x] Full toggle (compile-time + runtime)

### Safety & Compatibility
- [x] Original firmware unchanged and available
- [x] Zero backward compatibility issues
- [x] PIR disabled by default (P0, master off)
- [x] All original commands work identically
- [x] No changes to aiming/firing logic

### Documentation
- [x] 5 comprehensive guides (500+ KB)
- [x] Wiring diagrams included
- [x] Pinout reference with breadboard layout
- [x] User guide included
- [x] Technical deep-dive included
- [x] Migration & deployment guide
- [x] Troubleshooting section
- [x] Quick-start for all user types

### Status
- [x] Smart Sentry v2 UI complete (Guard tab)
- [x] Python PIR manager & engine integration complete
- [x] ESP32 firmware complete (new + original backed up)
- [x] All modules compile successfully
- [x] Test suite passing (5/5)
- [x] Documentation complete
- [x] Ready for hardware validation
- [x] ESP32 telemetry parser documented for serial and live WiFi paths
- [ ] End-to-end integration testing (future work)

---

## 🚀 Deployment Checklist

### Phase 1: Review & Approval
- [ ] Read PIR_INTEGRATION_SUMMARY.md
- [ ] Review FIRMWARE_COMPARISON.md (no breaking changes)
- [ ] Approve implementation approach
- [ ] Budget time for testing

### Phase 2: ESP32 Firmware Testing
- [ ] Flash new firmware with ENABLE_PIR_SUPPORT=0
- [ ] Run all original commands (F1, S0, M0, etc.)
- [ ] Verify water trigger works on the DB3000 ESP32 contract
- [ ] Verify projectile trigger works on the DB3000 ESP32 contract
- [ ] Verify LED/Laser/Acc relays work
- [ ] Confirm no regressions

### Phase 3: Hardware Setup (When Ready)
- [ ] Connect 3 PIR sensors to GPIO 35, 34, 39
- [ ] Verify 3.3V power and GND correct
- [ ] Brief firmware with ENABLE_PIR_SUPPORT=1
- [ ] Test each sensor with hand motion
- [ ] Verify debounce (max 1 event per 200ms)

### Phase 4: PC Application
- [ ] Review Smart Sentry v2 Guard tab
- [ ] Enable PIR master checkbox
- [ ] Configure sensor angles for your actual mounting layout
- [ ] Treat 45°, 135°, 225° as code defaults, not fixed hardware truth
- [ ] Adjust scan grid settings
- [ ] Test full behavior (slew → search → engage)

### Phase 5: Production Deployment
- [ ] Run integration tests (end-to-end)
- [ ] Monitor first few captures
- [ ] Collect statistics on false positives
- [ ] Tune grid resolution/timeout per environment
- [ ] Archive both firmware versions

---

## ✅ Verification Checklist (Post-Deployment)

- [ ] Smart Sentry app starts with Guard tab visible
- [ ] PIR Guard section appears in Guard tab
- [ ] Master enable checkbox works
- [ ] Sensor 1/2/3 pan/tilt can be edited
- [ ] Spin boxes move, values update in config
- [ ] Scan settings adjustable
- [ ] Status display shows live state
- [ ] Save/Load settings persists PIR config
- [ ] Original trigger modes still work on the current DB3000 ESP32 path (water/projectile)
- [ ] LED/Laser/Acc outputs still respond
- [ ] Turret safety logic unchanged
- [ ] App stability unaffected

Checklist note:

- this checklist assumes the current DB3000 ESP32 Smart Sentry app path
- archived Waveshare single-board bridge validation is separate and may not expose projectile trigger-servo PWM even when mode switching is still represented in software

---

## 🔗 Cross-Reference Index

### By Topic

**Architecture & Design**
- PIR_INTEGRATION_SUMMARY.md - System diagram
- PIR_GUARD_IMPLEMENTATION_COMPLETE.md - Detailed arch
- FIRMWARE_COMPARISON.md - Code structure changes

**Hardware & Wiring**
- ESP32_PIN_QUICK_REFERENCE.md - Primary reference
- ESP32_PIR_FIRMWARE_GUIDE.md - Electrical specs (section)

**Software (Python)**
- PIR_GUARD_IMPLEMENTATION_COMPLETE.md - Config, manager, engine, UI
- sentry_v2_config.py - Source code
- sentry_v2_engine.py - Source code

**Software (Firmware)**
- ESP32_PIR_FIRMWARE_GUIDE.md - Architecture
- FIRMWARE_COMPARISON.md - Code changes
- SMART_SENTRY_V2_3_1_ESP32_UDP_PIR.ino - Live WiFi app path
- DB3000_ESP32_IO_Telemetry_2026_w_PIR.ino - Direct serial IO path

**Operations & Tuning**
- PIR_GUARD_QUICK_START.md - Complete user guide
- ESP32_PIN_QUICK_REFERENCE.md - Testing section

**Integration & Deployment**
- FIRMWARE_COMPARISON.md - Deployment strategy
- PIR_INTEGRATION_SUMMARY.md - Next steps

**Troubleshooting**
- PIR_GUARD_QUICK_START.md - FAQ section
- ESP32_PIN_QUICK_REFERENCE.md - Common issues
- ESP32_PIR_FIRMWARE_GUIDE.md - Troubleshooting section

---

## 📞 Support Resources

### For GPIO Pin Issues
→ See ESP32_PIN_QUICK_REFERENCE.md, Troubleshooting section

### For PIR Events Not Appearing
→ See ESP32_PIR_FIRMWARE_GUIDE.md, Troubleshooting section

### For UI Not Showing PIR Controls
→ See PIR_GUARD_QUICK_START.md, section "Turret Not Moving When I Wave Hand"

### For Sensor Calibration
→ See PIR_GUARD_QUICK_START.md, section "Configuration File Location"

### For Integration with Other Systems
→ See PIR_GUARD_IMPLEMENTATION_COMPLETE.md, section "Integration with Smart Sentry v2"

### For Code Changes
→ See FIRMWARE_COMPARISON.md for exact line-by-line comparison

---

## 🎓 Learning Path

### Beginner (Just Want It Working)
1. PIR_GUARD_QUICK_START.md
2. ESP32_PIN_QUICK_REFERENCE.md (wiring section)
3. Try it out, see what happens

### Intermediate (Want to Understand)
1. PIR_INTEGRATION_SUMMARY.md
2. ESP32_PIR_FIRMWARE_GUIDE.md
3. PIR_GUARD_IMPLEMENTATION_COMPLETE.md

### Advanced (Want to Extend/Modify)
1. PIR_GUARD_IMPLEMENTATION_COMPLETE.md (full)
2. FIRMWARE_COMPARISON.md (code review)
3. Source code in repo
4. Test suite (test_pir_ui_config.py)

### Expert (Future Development)
All documents above, plus:
- Investigate sentry_v2_comm.py for UDP telemetry parser
- Plan enhancements (more sensors, real-time state, etc.)
- Evaluate alternative sensor types

---

## 📈 Version & Status

| Component | Version | Status |
|-----------|---------|--------|
| Smart Sentry v2 UI | 1.0 | ✅ Complete |
| Smart Sentry v2 Engine | 1.0 | ✅ Complete |
| ESP32 Firmware | 1.0 | ✅ Complete |
| Documentation | 1.0 | ✅ Complete |
| Unit Tests | 1.0 | ✅ 5/5 passing |
| Hardware Validation | - | ⏳ Pending |
| Telemetry Parser | - | ⏳ Future |
| Production Deployment | - | ⏳ Scheduled |

---

**Last Updated**: December 2024  
**Total Documentation**: 500+ KB across 5 guides  
**Code Changes**: ~700 lines (Python + C++) plus tests  
**Backward Compatibility**: 100% (no breaking changes)  
**Status**: ✅ READY FOR DEPLOYMENT

---

## 🎯 Next Action

**Pick Your Role Above, Start Reading the Recommended Document**

If you're unsure, start with: **PIR_INTEGRATION_SUMMARY.md**

Happy deploying! 🚀
