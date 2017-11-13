# -*- coding: utf-8 -*-

# tooltip.py

import sys
#from PyQt4.QtGui import *
#from PyQt4 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Tooltip(QWidget):
    def __init__(self,  parent=None):
        QWidget.__init__(self, parent)
        
        self.setGeometry(300,  300,  250,  150)
        self.setWindowTitle('Tooltip')
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        QToolTip.setFont(QFont('OldEnglish',  10))



app = QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec())


