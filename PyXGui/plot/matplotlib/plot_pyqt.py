# Object-oriented plot
# Refer to http://www.cnblogs.com/vamei/archive/2013/01/30/2879700.html

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import time, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Plot(QWidget):

    def __init__(self, parent=None):
        super(Plot, self).__init__(parent)

        fig = Figure(facecolor='#AABBCC')
        self.canvas = FigureCanvas(fig)

        # first axes
        ax1 = fig.add_axes([0.1, 0.1, 0.2, 0.2])
        line, = ax1.plot([0, 1], [0, 1])
        ax1.set_title('a strait line (OO)')
        ax1.set_xlabel('x value')
        ax1.set_ylabel('y value')

        # second axes
        ax2 = fig.add_axes([0.1, 0.4, 0.4, 0.5])
        sca = ax2.scatter([1, 3, 5], [2, 1, 2])
        line2, = ax2.plot([0, 1, 2, 3], [0, 2, 3, 4])
        line2.set_color('g')
        ax2.set_title('ax2')
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.grid()

        # third axes
        ax3 = fig.add_axes([0.55, 0.4, 0.4, 0.5])
        x = [1, 2, 3]
        y = [4, 5, 6]
        ax3.bar(x, y)

        # ax4 = fig.add_axes([0.5, 0.1, 0.2, 0.2])
        # ax4.pie(x, y)

        self.initUI()

        # canvas.plot()
        # print(line.__class__.__name__)

        # canvas.show()
        # time.sleep(3)

        # print(line.findobj())
        # canvas.print_figure('demo.jpg')

    def initUI(self):
        self.canvas.draw()
        layout = QHBoxLayout(self)
        layout.addWidget(self.canvas)
        self.setWindowTitle('Object-oriented Matplotlib with PyQt example')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Plot()
    # ui.show()
    sys.exit(app.exec())
