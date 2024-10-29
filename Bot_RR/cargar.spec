# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['cargar.py'],
             pathex=['C:/Users/prueba/AppData/Local/Programs/Python/Python38/Lib/site-packages/autoit'],
             binaries=[('C:/Users/prueba/AppData/Local/Programs/Python/Python38/Lib/site-packages/autoit/lib/AutoItX3.dll', '/lib'), ('C:/Users/prueba/AppData/Local/Programs/Python/Python38/Lib/site-packages/autoit/lib/AutoItX3_x64.dll', '/lib')],
             datas=[],
             hiddenimports=['autoit'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='cargar',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
