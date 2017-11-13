#from PyQt4.QtGui import *
#from PyQt4.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.resize(250, 150)
        self.setWindowTitle('statusbar & menubar')
        
        self.statusBar().showMessage('Ready')
        
        exit = QAction(QIcon('icons/exit.png'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
#        self.connect(exit, SIGNAL('triggered()'), SLOT('close()'))
        exit.triggered.connect(self.close)
        
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)
        edit = menubar.addMenu('&Edit')
        view = menubar.addMenu('&View')

app = QApplication(sys.argv)
mw = MainWindow()
mw.show()

sys.exit(app.exec())
