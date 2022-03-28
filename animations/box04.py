import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

ax.set_facecolor(color='black')

ax.plot(1, 1, 'o', color='black', markersize=1)

ax.plot(1000, 1000, 'o', color='black', linewidth=2, markersize=1)

# start_x = 0
# end_x = 1000
# velocity = 1.0
# acceleration = 0
# pos = start_x
# dt = 1
#
#
# while pos < end_x:
#     dist = ((end_x-start_x)/2 - pos)
#     velocity = velocity + dist * 0.001
#     # if dist > (end_x - start_x) / 2:
#     #     velocity = velocity + dist * 0.001
#     # else:
#     #     velocity = velocity - dist * 0.001
#
#     pos = pos + velocity * dt
#     print(f"pos={pos}  vel={velocity}")

start_x = 0
end_x = 1000
velocity = 1.0
pos = start_x
dt = 1

last_pos = pos

def animate2(i):
    global start_x, end_x, velocity, pos, dt, last_pos
    # point from (0,500) to (1000,500) with acceleration and then deceleration

    # if pos > 1000:
    #     return

    dist = ((end_x - start_x) / 2 - pos)
    velocity = velocity + dist * 0.001
    if velocity < 0:
        velocity = 0.1

    pos = pos + velocity * dt
    print(f"pos={pos}  vel={velocity} i={i}")

    if pos > 1000:
        return

    # ax.plot(pos, 500, 'o', color='#0abab5', linewidth=5, markersize=1)
    # ax.plot([last_pos, pos], [500, 500], color='#0abab5', linewidth=5, markersize=1)

    ax.add_patch(Rectangle((last_pos, 500), width=pos-last_pos, height=300,
                           facecolor='#0abab5',
             fill=True))

    last_pos = pos


ani = animation.FuncAnimation(
    fig, animate2, frames=100,
    interval=10, blit=False, save_count=100, repeat=False)

plt.show()
