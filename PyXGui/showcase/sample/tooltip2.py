#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
ZetCode PyQt4 tutorial
This example shows a tooltip on
a window and a button
author: Jan Bodnar
website: zetcode.com
last edited: October 2011
"""
import sys
#from PyQt4 import QtGui
from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')
        self.show()
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
