import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp


t=np.arange(-10,10,0.1)
delta = np.pi/2
periods = [(3,2), (3,4), (5,4), (5,6)]

for p in periods:
    fig, ax = plt.subplots()
    ax.plot(np.sin(p[0] * t + delta), np.cos(p[1] * t), label=f'Частота ({p[0]}, {p[1]})')
    ax.legend()

    plt.grid()
    plt.savefig(f'lab_10/task2#{p[0]}{p[1]}.png')

