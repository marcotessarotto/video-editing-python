import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots()


ax.set_facecolor(color='black')

ax.plot(1, 1, 'ro', markersize=1)

ax.plot(1000, 1000, 'ro', linewidth=2, markersize=1)

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

def animate2(i):
    global start_x, end_x, velocity, pos, dt
    # point from (100,100) to (900,100) with acceleration and deceleration

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

    ax.plot(pos, 500, 'o', color='#0abab5', linewidth=5, markersize=1)


ani = animation.FuncAnimation(
    fig, animate2, frames=100,
    interval=10, blit=False, save_count=100, repeat=False)


plt.show()
