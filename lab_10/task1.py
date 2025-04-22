import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp


t=np.arange(-1,1,0.001)
fig, ax = plt.subplots()

for n in range(1,8):

    form = sp.legendre(n)
    ax.plot(t, form(t), linewidth=2, label = f'n={n}')
    ax.legend()

plt.title('Полиномы Лежандра')
plt.grid()
plt.savefig("lab_10/task1.png")

