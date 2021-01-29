# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['src/jaeger_grpc_server/main.py'],
             pathex=['/Users/jzam/projects/jaeger_server_python'],
             binaries=[],
             datas=[],
             hiddenimports=[
                'colorsys', 'decimal', 'json', 'ipaddress', 'pathlib', 'uuid',
                'dataclasses',  'dns'
             ],
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
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
