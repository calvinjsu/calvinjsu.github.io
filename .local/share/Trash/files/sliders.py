import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
import scipy as sp

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
plt.xlim(-100, 100)
plt.ylim(-10000, 10000)
plt.grid()
plt.title("a * x^2 + b * x + c")

a0, b0, c0 = 1, 2, 1  # parameters
x = np.arange(-100, 100, 0.01)
y = a0*x**2 + b0*x + c0  # function
p, = plt.plot(x, y)
ax.margins(x=0)

# axes for sliders
axcolor = 'lightgoldenrodyellow'
axa = plt.axes([0.185, 0.15, 0.65, 0.03], facecolor=axcolor)
axb = plt.axes([0.185, 0.1, 0.65, 0.03], facecolor=axcolor)
axc = plt.axes([0.185, 0.05, 0.65, 0.03], facecolor=axcolor)
# sliders (just visual for now)
slia = Slider(axa, 'a', -10.0, 10.0, valinit=a0, valstep=0.1)
slib = Slider(axb, 'b', -250.0, 250.0, valinit=b0, valstep=1)
slic = Slider(axc, 'c', -5000.0, 5000.0, valinit=c0, valstep=10)

# update procedure


def up(val):
    a = slia.val
    b = slib.val
    c = slic.val
    p.set_ydata(a*x**2 + b*x + c)
    fig.canvas.draw_idle()


# sliders become active
slia.on_changed(up)
slib.on_changed(up)
slic.on_changed(up)


plt.show()
