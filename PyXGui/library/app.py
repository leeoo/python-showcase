# -*- coding: utf-8 -*-


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys, os.path


# Define function to import external files when using PyInstaller.
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')

    print('base_path -> %s, relative_path -> %s' % (base_path, relative_path))
    return os.path.join(base_path, relative_path)


class AppWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        print('library')
        uic.loadUi(resource_path('library.ui'), self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_window = AppWindow()
    app_window.show()
    sys.exit(app.exec())
