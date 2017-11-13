打包命令


pyinstaller -D -w --clean --noconfirm --add-data="logging.ini:." --add-data="pyinstaller_demo.ui:." --add-data="config.ini:."  -p "." app.py

pyinstaller -D -w --clean --noconfirm --add-data="config/:config/" --add-data="app.log:." --add-data="pyinstaller_demo.ui:." --add-data="config.ini:."  -p "." app.py
