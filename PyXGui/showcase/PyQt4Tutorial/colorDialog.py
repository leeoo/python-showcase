# -*- coding: utf-8 -*-

# QColorDialog

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        color = QColor(0, 0, 0)
        
        self.button = QPushButton('Dialog', self)
        
        self.button.setFocusPolicy(Qt.NoFocus)
        self.button.move(20, 20)
        self.button.clicked.connect(self.showDialog)
        self.setFocus()
        
        self.widget = QWidget(self)
        self.widget.setStyleSheet('QWidget {background-color: %s}'
            % color.name())
        self.widget.setGeometry(130, 22, 100, 100)
        
        self.setWindowTitle('ColorDialog')
        self.setGeometry(300, 300, 250, 180)


    def showDialog(self):
        col = QColorDialog.getColor()
        
        if col.isValid():
            self.widget.setStyleSheet('QWidget {background-color: %s}'
            % col.name())


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
