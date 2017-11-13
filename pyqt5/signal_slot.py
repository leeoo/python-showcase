#!/bin/python
# -*- coding: utf-8 -*-


import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        lcd = QLCDNumber()
        sld = QSlider(Qt.Horizontal)

        button1 = QPushButton('Button1', self)
        button2 = QPushButton('Button2', self)

        button1.move(30, 50)
        button1.move(80, 50)

        vbox = QHBoxLayout(self)
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        vbox.addWidget(button1)
        vbox.addWidget(button2)

        sld.valueChanged.connect(lcd.display)

        button1.clicked.connect(self.click_button)
        button2.clicked.connect(self.click_button)

        self.statusBar()
        self.setGeometry(300, 300, 290, 150)

        self.setLayout(vbox)
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def click_button(self, value):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was processed!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    # window
    sys.exit(app.exec())