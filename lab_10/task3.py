import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp
from matplotlib.animation import FuncAnimation


fig,ax = plt.subplots()

delta = np.pi/2
t=np.arange(-50,50,0.1)
curve, = plt.plot([], [])

def draw(i):
    a=1-i*0.001

    x=[np.sin(a*j + delta) for j in t]
    y=[np.cos(j) for j in t]

    return x,y

def animate(i):
    curve.set_data(draw(i))

ani = FuncAnimation(fig, animate, frames=1000)
plt.xlim(-1,1)
plt.ylim(-1,1)

ani.save("lab_10/task3.gif")