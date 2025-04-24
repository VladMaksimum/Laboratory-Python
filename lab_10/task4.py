import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


def wave(t, freq, ampl):
    return ampl * np.sin(2* np.pi * freq * t)

freq0 = 5
ampl0 = 3

t = np.linspace(0, 1, 1000)

#Волна 1
fig, ax = plt.subplots()
line1, = plt.plot(t, wave(t, freq0, ampl0))

freq_slider1 = Slider(fig.add_axes([0.25, 0.1, 0.65, 0.03]), label='Frequency', valmin=0.1, valmax=30, valinit=freq0)
ampl_slider1 = Slider(fig.add_axes([0.1, 0.25, 0.0225, 0.63]), label="Amplitude", valmin=0, valmax=10, valinit=ampl0, orientation="vertical")

fig.subplots_adjust(left=0.25, bottom=0.25)

def update(val):
    line1.set_ydata(wave(t, freq_slider1.val, ampl_slider1.val))
    summ.set_ydata([(line1.get_ydata()[i] + line2.get_ydata()[i]) for i in range(len(t))])
    fig.canvas.draw_idle()

freq_slider1.on_changed(update)
ampl_slider1.on_changed(update)


#Волна 2
fig, ax = plt.subplots()
line2, = plt.plot(t, wave(t, freq0, ampl0))

freq_slider2 = Slider(fig.add_axes([0.25, 0.1, 0.65, 0.03]), label='Frequency', valmin=0.1, valmax=30, valinit=freq0)
ampl_slider2 = Slider(fig.add_axes([0.1, 0.25, 0.0225, 0.63]), label="Amplitude", valmin=0, valmax=10, valinit=ampl0, orientation="vertical")

fig.subplots_adjust(left=0.25, bottom=0.25)

def update(val):
    line2.set_ydata(wave(t, freq_slider2.val, ampl_slider2.val))
    summ.set_ydata([(line1.get_ydata()[i] + line2.get_ydata()[i]) for i in range(len(t))])
    fig.canvas.draw_idle()

freq_slider2.on_changed(update)
ampl_slider2.on_changed(update)


#Сумма
fig, ax = plt.subplots()
points=[(line1.get_ydata()[i] + line2.get_ydata()[i]) for i in range(len(t))]

summ, = plt.plot(t, points)

plt.show()
