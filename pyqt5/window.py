#!/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.create_ui()

    def create_ui(self):
        click_me = QPushButton('Click me!', self)
        vbox = QVBoxLayout(self)
        vbox.addWidget(click_me)
        # self.layout().addWidget(click_me)
        self.setLayout(vbox)

        self.setWindowTitle('PyQt5示例1')
        self.show()
        click_me.clicked.connect(self.show_dialog)

    def show_dialog(self):
        print('show dialog after click button')
        dialog = QDialog(self)
        dialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    # window.setWindowTitle()
    # window.show()
    sys.exit(app.exec())
