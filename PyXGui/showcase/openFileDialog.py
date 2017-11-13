# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.setFocus()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showFileDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(350, 350, 400, 300)
        self.setWindowTitle('Show file dialog')


    def showFileDialog(self):
        #file, ok = QFileDialog().getOpenFileName(self, 'Open file', 'C:\Apply')
        #if ok:
        #    print('Open file with name: %s' % file)
        #    pass
        filename = QFileDialog().getOpenFileName(self, 'Open file', 'C:\Apply')
        print(filename)
        f = open(filename)
        data = f.read()
        self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())