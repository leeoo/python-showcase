# object-oriented plot
# Refer to http://www.cnblogs.com/vamei/archive/2013/01/30/2879700.html

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.path import Path
import matplotlib.patches as patches


fig = Figure()
canvas = FigureCanvas(fig)
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

vertices = [
    (0., 0.),
    (0., 1.),
    (0.5, 1.5),
    (1., 1.),
    (1., 0.),
    (0., 0.),
]

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

# codes = [Path.MOVETO,
#          Path.CURVE3,
#          Path.CURVE3,
#          Path.CURVE3,
#          Path.CURVE3,
#          Path.CLOSEPOLY,
#          ]

path = Path(vertices, codes)

patch = patches.PathPatch(path, facecolor='coral')
ax.add_patch(patch)
ax.set_xlim(-0.5, 2)
ax.set_ylim(-0.5, 2)

canvas.print_figure('demo.jpg')
