__author__ = 'Lex'

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
# import test
# import autoFillLayout
import customTitleBar


class MainForm(QMainWindow):
    def __init__(self, parent=None):
        # QMainWindow.__init__(self, parent)
        super(MainForm, self).__init__(parent)
        self.ui = customTitleBar.Ui_MainWindow()
        self.ui.setupUi(self)

        # TODO 使用系统内置的按钮来作为自定义标题栏的最小、最大及关闭按钮
        self.ui.minPixmap = QPixmap()
        self.ui.maxPixmap = QPixmap()
        self.ui.closePixmap = QPixmap()
        # minBtn = QToolButton()
        # maxBtn = QToolButton()
        # closeBtn = QToolButton()

        # TODO Apply internal Qt Style Sheet
        # self.ui.minButton.setStyleSheet('''
        #     QPushButton{color: red}
        # ''')

        # TODO Apply external Qt Style Sheet
        styleFile = QFile('metro.qss')
        styleFile.open(QFile.ReadOnly)
        styleSheet = styleFile.readAll()
        styleSheet = str(styleSheet, encoding='utf-8')
        qApp.setStyleSheet(styleSheet)

        self.ui.minButton.clicked.connect(self.showMinimized)
        self.ui.maxButton.clicked.connect(self.clickMaxButton)
        self.ui.closeButton.clicked.connect(self.close)
        self.ui.titleBarLabel.setText('Frameless PyQt')

        # TODO Test
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)

        self.m_DragPosition = self.pos()

        # self.ui = autoFillLayout.Ui_MainWindow()

        # self.ui = autoFillLayout.Ui_Form()
        # self.ui.setupUi(self)

    def clickMaxButton(self):
        if self.isMaximized():
            print('Show form window from max to normal')
            self.showNormal()
        else:
            print('Show form window from normal to max')
            self.showMaximized()


    def mousePressEvent(self, event):
        QMainWindow.mousePressEvent(self, event)
        if event.button()  == Qt.LeftButton:
            print('mouse press')
            self.m_drag = False
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

app = QApplication(sys.argv)
main = MainForm()
main.show()

sys.exit(app.exec())
