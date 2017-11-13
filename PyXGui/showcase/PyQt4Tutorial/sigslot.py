# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)
#        slider = QSlider(Qt.Vertical, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        slider.valueChanged.connect(lcd.display)
        
        self.setWindowTitle('Signal & Slot')
        self.resize(250, 150)

app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
