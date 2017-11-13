# -*- mode: python -*-

block_cipher = None


a = Analysis(['matplot_on_pyqt.py'],
             pathex=['/Users/libo/workshop/Python/PyXGui/plot/matplotlib'],
             binaries=[],
             datas=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='matplot_on_pyqt',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='matplot_on_pyqt.app',
             icon=None,
             bundle_identifier=None)
