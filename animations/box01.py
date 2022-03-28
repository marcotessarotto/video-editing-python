import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# figure and axis (area to plot on)
fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
# print(x)
# print(np.sin(x))

# line, = ax.plot(x, np.sin(x))
#
# print(line)
#
# line, = ax.plot([80, 20], [100, 100], color='#0abab5', linewidth=5)
#
# plt.show()
#
# exit(0)

ax.set_facecolor(color='black')

ax.plot(1, 1, 'ro', markersize=1)

ax.plot(100, 100, 'ro', linewidth=2, markersize=1)


# ax.plot([1, 2], [1, 1], color='#0abab5', linewidth=5)

# def animate(i):
#     line.set_ydata(np.sin(x + i / 50))  # update the data.
#     return line,


def animate2(i):
    # line2, = ax.plot([80, 80-i], [100, 100], color='#0abab5', linewidth=5)
    line2, = ax.plot([80 - i + 1, 80 - i], [100, 100], color='#0abab5', linewidth=5)
    return line2,


ani = animation.FuncAnimation(
    fig, animate2, frames=50,
    interval=100, blit=False, save_count=50, repeat=False)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
