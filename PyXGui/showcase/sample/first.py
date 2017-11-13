# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtGui

app = QtGui.QGuiApplication(sys.argv)
label = QtGui.QLabel("Hello Qt!")
label.show()
sys.exit(app.exec_())