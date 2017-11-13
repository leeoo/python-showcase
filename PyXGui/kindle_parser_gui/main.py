"""
@author: Lex
@version: 1.0, 2014/12/1
"""


import sys, os, logging
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main_form import Ui_MainWindow


class KindleParserGui(QWidget):
    def __init__(self, parent=None):
        super(KindleParserGui, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bindSignalSlots()

    def bindSignalSlots(self):
        self.ui.selectDirectory.clicked.connect(self.selectSingleDirectory)
        self.ui.selectFile.clicked.connect(self.selectSingleFile)
        self.ui.selectFiles.clicked.connect(self.selectMultiFiles)

    def selectSingleDirectory(self):
        _dirname = QFileDialog.getExistingDirectory(self, ('选择文件夹..'), \
                                                 'C:/Users/leeoo/Downloads')
        self.ui.directoryNameEdit.setText(_dirname)

    def selectSingleFile(self):
        _filename = QFileDialog.getOpenFileName(self, ('选择文件..'), \
                                                 'C:/Users/leeoo/Downloads', ('(epub文件 (*.epub))'))
        filename_ = _filename[0]
        self.ui.filenameEdit.setText(filename_)

    def selectMultiFiles(self):
        _filename = QFileDialog.getOpenFileNames(self, ('选择文件..'), \
                                                 'C:/Users/leeoo/Downloads', ('(epub文件 (*.epub))'))
        filename_ = _filename[0]
        for filename in filename_:
            self.ui.fileListWidget.addItem(filename)



def main():
    app = QApplication(sys.argv)
    form = KindleParserGui()
    form.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()