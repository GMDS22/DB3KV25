# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import collect_all

datas = [
    ('app/sentry_v2', 'app/sentry_v2'),
    ('app/config', 'app/config'),
    ('YOLO_MODELS', 'YOLO_MODELS'),
    ('app/LOGO.png', 'app/LOGO.png'),
    ('requirements-sentry-v2-portable.txt', 'requirements-sentry-v2-portable.txt'),
    ('SENTRY_V2_PORTABLE_INCLUDE_LIST.md', 'SENTRY_V2_PORTABLE_INCLUDE_LIST.md'),
    ('SENTRY_V2_PORTABLE_FIX_LOG_2026-03-24.md', 'SENTRY_V2_PORTABLE_FIX_LOG_2026-03-24.md'),
]
binaries = []
hiddenimports = []
tmp_ret = collect_all('ultralytics')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('yt_dlp')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['run.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib.tests', 'pytest'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SMART_SENTRY',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='SMART_SENTRY',
)
