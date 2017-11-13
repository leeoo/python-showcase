# -*- coding: utf-8 -*-

# richTooltip

import sys
#from PyQt4.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyTooltip(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        self.setGeometry(300,  300,  300,  200)
        self.setWindowTitle('Test tooltip.')
        self.setToolTip('test <color>tooltip</color> widget')
        QToolTip.setFont(QFont('asgasdgasg',  10))

app = QApplication(sys.argv)
tip = MyTooltip()
tip.show()
sys.exit(app.exec_())
