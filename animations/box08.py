import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
from matplotlib.transforms import Bbox, TransformedBbox
from matplotlib.figure import Figure
from matplotlib.text import Text, Annotation

# https://matplotlib.org/stable/api/text_api.html

fig: Figure

fig, ax = plt.subplots()

ax.set_facecolor(color='white')

ax.plot(1, 1, 'o', color='black', markersize=1)

ax.plot(1000, 1000, 'o', color='white', linewidth=2, markersize=1)

font_dict = {'family':'serif',
                 'color':'darkred',
                 'size':15}

ax.annotate('local max', xy=(3, 1),  xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top'
            )

txt = ax.text(200, 100,'Text Example', fontdict=font_dict, )


# annotation = Annotation(
#         '', xy=(0.0, 50.0), xytext=(50.0, 50.0), xycoords='figure pixels',
#         arrowprops={
#             'facecolor': 'white', 'width': 108, 'headwidth': 10, 'shrink': 0.0})
# annotation.set_figure(fig)

    # annotation.draw(renderer)

plt.show()