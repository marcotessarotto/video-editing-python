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

ax.plot(1000, 1000, 'ro', linewidth=2, markersize=1)


# ax.plot([1, 2], [1, 1], color='#0abab5', linewidth=5)

# def animate(i):
#     line.set_ydata(np.sin(x + i / 50))  # update the data.
#     return line,

A = 500
B = 200

STARTX = 800
STARTY = 800


def animate2(i):
    # print(i)
    i = i * 10

    global A, B, STARTX, STARTY
    # line2, = ax.plot([80, 80-i], [100, 100], color='#0abab5', linewidth=5)

    if i <= A:
        # upper horizontal line
        ax.plot(STARTX-i, STARTY, 'o', color='#0abab5', linewidth=5, markersize=1)

    if i <= B:
        # right vertical line
        ax.plot(STARTX, STARTY-i, 'o', color='#0abab5', linewidth=5, markersize=1)

    if i >= B:
        if i <= A+B:
            # lower horizontal line
            ax.plot(STARTX-i+B, STARTY-B, 'o', color='#0abab5', linewidth=5, markersize=1)

    if A <= i <= A+B:
        ax.plot(STARTX-A, STARTY - i + A, 'o', color='#0abab5', linewidth=5, markersize=1)

    if B <= i <= 2*B:
        # diagonal lines
        ax.plot([STARTX- (i-B), STARTX],[STARTY, STARTY - (i-B)], color='#0abab5', linewidth=1)

    if 2*B <= i <= A+B:
        # diagonal lines
        ax.plot([STARTX-i+2*B - B,STARTX-i+2*B],[STARTY, STARTY-B], color='#0abab5', linewidth=1)

    # if 2*B <= i:
    #



    #line2, = ax.plot([80 - i + 1, 80 - i], [100, 100], color='#0abab5', linewidth=5)
    return


r = range(1,1000,10)

ani = animation.FuncAnimation(
    fig, animate2, frames=len(r),
    interval=100, blit=False, save_count=1000, repeat=False)

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
