import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
from matplotlib.transforms import Bbox, TransformedBbox
from matplotlib.figure import Figure
from matplotlib.text import Text

fig: Figure

fig, ax = plt.subplots()
# print(fig)
fig_win_ext = fig.get_window_extent()
print(fig_win_ext)
print(f"fig_win_ext.x0={fig_win_ext.x0} fig_win_ext.x1={fig_win_ext.x1}")

ax.set_facecolor(color='black')

# ax.plot(1, 1, 'o', color='black', markersize=1)
#
# ax.plot(1000, 1000, 'o', color='black', linewidth=2, markersize=1)


rectangle_height = 300
start_y = 500

start_x = 1000
end_x = 0
velocity = 0.0
pos = start_x
dt = 1

last_pos = pos

# max_figure_x = max(start_x, end_x)
txt: Text
txt = plt.text(start_x, start_y + rectangle_height / 2, "I am Adding Text To The Plot", color='white')
txt.set_color('green')
txt.set_visible(True)
plt.pause(0.1) # we need to show text in order to get window extent (below)

txt_win_ext_orig: Bbox
txt_win_ext_orig = txt.get_window_extent()

txt.set_visible(False)
plt.pause(0.1)
#
# txt_win_ext = txt.get_window_extent()
# print(txt_win_ext)
# plt.pause(1)
# exit(0)

def animate2(i):
    global start_x, end_x, velocity, pos, dt, last_pos, rectangle_height
    # move point from (0,500) to (1000,500) with acceleration and then deceleration

    dist = (abs(end_x - start_x) / 2 - pos)
    velocity = velocity + dist * 0.001
    # if velocity < 0:
    #     velocity = 0.1

    pos = pos + velocity * dt
    print(f"pos={pos}  vel={velocity} i={i}")

    if pos > 1000:
        return

    # ax.plot(pos, 500, 'o', color='#0abab5', linewidth=5, markersize=1)
    # ax.plot([last_pos, pos], [500, 500], color='#0abab5', linewidth=5, markersize=1)

    patch = ax.add_patch(Rectangle((last_pos, start_y), width=pos-last_pos, height=rectangle_height,
                           facecolor='#0abab5', fill=True))

    patch_win_ext = patch.get_window_extent()
    print(f"patch_win_ext = {patch_win_ext}")

    global txt, fig, fig_win_ext, txt_win_ext_orig

    txt_win_ext: Bbox
    fig_win_ext2: TransformedBbox
    box_pos = pos

    txt_win_ext = txt.get_window_extent()
    # print(txt_win_ext)
    fig_win_ext2 = fig.get_window_extent()
    # print(fig_win_ext2)
    print(f"fig_win_ext2.x0={fig_win_ext2.x0} fig_win_ext2.x1={fig_win_ext2.x1}")
    # print(fig_win_ext2.width)
    print(f"txt_win_ext_orig.x0 = {txt_win_ext_orig.x0} txt_win_ext_orig.x1 = {txt_win_ext_orig.x1} txt_win_ext.width={txt_win_ext_orig.width}")
    print(f"txt_win_ext.x0 = {txt_win_ext.x0} txt_win_ext.x1 = {txt_win_ext.x1} txt_win_ext.width={txt_win_ext.width}")

    # if txt_win_ext_orig.x1 > fig_win_ext2.x1:
    #     txt.set_visible(True)
    #     txt.set_x(txt_win_ext_orig.x0 - (fig_win_ext2.x1 - txt_win_ext_orig.x1))

    if not txt.get_visible() and txt_win_ext_orig.x1 > patch_win_ext.x1:
        txt.set_visible(True)
        txt_win_ext.x0 = txt_win_ext_orig.x0 - (txt_win_ext_orig.x1 - patch_win_ext.x1)
        print(f"moving back by {(txt_win_ext_orig.x1 - patch_win_ext.x1)}")
        print(txt_win_ext_orig.x0 - (txt_win_ext_orig.x1 - patch_win_ext.x1))
        print(txt_win_ext.x0)
        txt.set_x(txt_win_ext_orig.x0 - (txt_win_ext_orig.x1 - patch_win_ext.x1))

    # if box_pos + txt_win_ext.x1 - txt_win_ext.x0 > fig_win_ext2.x1:
    #     box_pos = txt_win_ext.x0 - (fig_win_ext2.x1 - txt_win_ext.x1)

    print(f"box_pos = {box_pos}")
    # print(txt)
    # print(we)
    # print(type(we))
    # if pos > 1000:

    # txt.set_x(box_pos)


    last_pos = pos


ani = animation.FuncAnimation(
    fig, animate2, frames=100,
    interval=1000, blit=False, save_count=100, repeat=False)



plt.show()
