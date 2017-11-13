# Object-oriented plot
# Refer to http://www.cnblogs.com/vamei/archive/2013/01/30/2879700.html

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import time


fig = Figure()
canvas = FigureCanvas(fig)

# first axes
ax1 = fig.add_axes([0.1, 0.1, 0.2, 0.2])
line, = ax1.plot([0, 1], [0, 1])
ax1.set_title('a strait line (OO)')
ax1.set_xlabel('x value')
ax1.set_ylabel('y value')

# second axes
ax2 = fig.add_axes([0.4, 0.3, 0.4, 0.5])
sca = ax2.scatter([1, 3, 5], [2, 1, 2])
ax2.set_title('ax2')

# canvas.plot()
print(line.__class__.__name__)

canvas.show()
time.sleep(3)

# print(line.findobj())
canvas.print_figure('demo.jpg')