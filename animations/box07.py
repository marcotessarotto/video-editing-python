# https://stackoverflow.com/questions/69473844/can-you-calculate-the-size-of-a-text-annotation-in-matplotlib

from matplotlib.figure import Figure as mpl_Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as mpl_Canvas

fig = mpl_Figure()
x, y, text = 5, 7, 'My label text'

fig.gca().plot(x, y, 'k.')
canvas = mpl_Canvas(fig)
t = fig.gca().text(x, y, text, color='red')
canvas.draw()

bbox = t.get_window_extent(renderer = canvas.get_renderer())
fig.gca().plot(
    [bbox.x0, bbox.x1, bbox.x1, bbox.x0, bbox.x0],
    [bbox.y0, bbox.y0, bbox.y1, bbox.y1, bbox.y0],
    'k:',
    transform=None)
canvas.print_figure("img.png")