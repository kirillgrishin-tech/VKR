# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
import glob,os
rasterio_imports_paths = glob.glob(r'C:\\Users\\grish\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\rasterio\\*.py')
rasterio_imports = ['rasterio._shim']

for item in rasterio_imports_paths:
    current_module_filename = os.path.split(item)[-1]
    current_module_filename = 'rasterio.'+current_module_filename.replace('.py', '')
    rasterio_imports.append(current_module_filename)


a = Analysis(['Main.py'],
             pathex=['C:\\Users\\grish\\Documents\\VKR\\WindMain'],
             binaries=[],
             datas=[],
             hiddenimports=rasterio_imports,
             hookspath=[],
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
          name='Main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='1.ico')
