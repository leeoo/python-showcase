打包命令


pyinstaller -D -w --clean --noconfirm --add-data="pyinstaller_demo.ui:." --add-data="config/config.ini:."  -p "." app.py

## works
pyinstaller -D -w --clean --noconfirm --add-data="pyinstaller_demo.ui:." --add-data="config/:config/" --add-data="config/config.ini:."  -p "." app.py
pyinstaller -D -w --clean --noconfirm --add-data="pyinstaller_demo.ui:." --add-data="config/:config/"  -p "." app.py
pyinstaller -D -w --clean --noconfirm --add-data="pyinstaller_demo.ui:." --add-data="config/:config/" app.py