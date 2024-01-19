import random
from collections import deque

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

time = [i / 10.0 for i in range(0, 2110)]
weight = np.interp(
    time,
    [0, 5, 30, 45, 60, 75, 90, 115, 210],
    [0, 75, 75, 175, 175, 275, 275, 357, 357],
)
index = 0


def simulate_weight():
    # Simulate weight measurement by incrementing the weight until it reaches 375 grams
    if 'last_weight' not in simulate_weight.__dict__:
        simulate_weight.last_weight = 0

    simulate_weight.last_weight += random.uniform(1, 3)  # Increment weight by a random value
    return min(simulate_weight.last_weight, 375)


def animate(i):
    global index
    index += 1
    if index >= len(time):
        x = time[len(time) - 1]
        y = weight[len(weight) - 1]
        data.append((x, y))
    else:
        x = time[index]
        y = weight[index]
        data.append((x, y))
    ax.relim()
    ax.autoscale_view()
    line.set_data(*zip(*data))


fig, ax = plt.subplots()
x = 0
y = 0
# plt.plot(time, weight)
data = deque([(x, y)])
(line,) = plt.plot(*zip(*data), c="black")


ani = animation.FuncAnimation(fig, animate, interval=16.66)
plt.show(block=True)
