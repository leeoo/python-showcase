# -*- mode: python -*-

block_cipher = None


a = Analysis(['library.py'],
             pathex=['/Users/libo/workshop/Python/PyXGui/library'],
             binaries=[],
             datas=[('library.ui', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='library',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='library')
app = BUNDLE(coll,
             name='library.app',
             icon=None,
             bundle_identifier=None)
