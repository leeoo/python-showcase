
# author: Lex
# version: 1.0


import random
import sys

from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import arange, sin, pi
# import matplotlib


class MyMplCanvs(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # self.axes.hold(False)  # 该方法已标注为过期，替代做法是在重画subplot前调用self.axes.clear()

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvs):
    '''静态画布： 一条正弦线'''
    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot = (t, s)


class MyDynamicMplCanvas(MyMplCanvs):
    '''动态画布：每秒自动更新，更换一条折线'''
    def __init__(self, *args, **kwargs):
        MyMplCanvs.__init__(self, *args, **kwargs)
        timer = QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self):
        random_int_nums = [random.randint(0, 10) for i in range(4)]

        self.axes.clear()  # 画之前将现有的图都清掉
        self.axes.plot([0, 1, 2, 3], random_int_nums, 'r')
        self.draw()


class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowTitle('程序主窗口')

        self.file_menu = QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 Qt.CTRL + Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QWidget(self)

        layout = QVBoxLayout(self.main_widget)
        static_canvas = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dynamic_canvas = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        layout.addWidget(static_canvas)
        layout.addWidget(dynamic_canvas)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        # 状态条显示2秒
        self.statusBar().showMessage('Matplotlib is good!', 2000)

    def fileQuit(self):
        self.close()

    def about(self):
        QMessageBox.about(self, 'About', '''关于。。。''')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ApplicationWindow()
    ui.setWindowTitle('PyQt5与Matplotlib例子')
    ui.show()
    sys.exit(app.exec())


