# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:/Projects_RPA/Estado_MER/Bot_RR/console.py'],
             pathex=['C:/Projects_RPA/x_old_proyects/TempNotasgenesisAs400-x/venv/Lib/site-packages/autoit/'],
             binaries=[('C:/Projects_RPA/x_old_proyects/TempNotasgenesisAs400-x/venv/Lib/site-packages/autoit/lib/AutoItX3.dll', '/lib'), ('C:/Projects_RPA/x_old_proyects/TempNotasgenesisAs400-x/venv/Lib/site-packages/autoit/lib/AutoItX3_x64.dll', '/lib')],
             datas=[],
             hiddenimports=[],
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
          name='console',
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
          entitlements_file=None , icon='C:\\Projects_RPA\\Estado_MER\\Bot_RR\\imagen\\troncales.ico')
