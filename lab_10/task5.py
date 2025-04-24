import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y= np.arange(0,10,0.1)
x,y = np.meshgrid(x,y)
z= ((x-3)**2 + (y-2)**2)/2

fig,ax = plt.subplots(subplot_kw={"projection":"3d"})
ax.plot_surface(x,y,z)
ax.set_zlim(-10,10)
plt.savefig("lab_10/task5.png")

fig,ax = plt.subplots(subplot_kw={"projection":"3d"})
ax.set_zlim(-10,10)
ax.plot(x,y,np.log(z))
plt.savefig("lab_10/task5log.png")
