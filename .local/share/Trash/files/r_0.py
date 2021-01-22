import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np
import scipy as sp

beta = 0.75
sigma = 0.25
gamma = 0.33
death = 0.05

S = [49]
E = [0]
I = [1]
R = [0]


def dS(S, E, I, R, beta, sigma, gamma):
    return -beta*S*I/(S+E+I+R)


def dE(S, E, I, R, beta, sigma, gamma):
    return beta*S*I/(S+E+I+R) - sigma*E


def dI(S, E, I, R, beta, sigma, gamma, death):
    return sigma*E - gamma*I - death*I


def dR(S, E, I, R, beta, sigma, gamma):
    return gamma*I


fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

for i in range(100):
    S.append(S[i]+dS(S[i], E[i], I[i], R[i], beta, sigma, gamma))
    E.append(E[i]+dE(S[i], E[i], I[i], R[i], beta, sigma, gamma))
    I.append(I[i]+dI(S[i], E[i], I[i], R[i], beta, sigma, gamma, death))
    R.append(R[i]+dR(S[i], E[i], I[i], R[i], beta, sigma, gamma))

N = []
for i in range(101):
    N.append(S[i]+E[i]+I[i]+R[i])

s, = plt.plot(range(101), S, label="S")
e, = plt.plot(range(101), E, label="E")
ie, = plt.plot(range(101), I, label="I")
r, = plt.plot(range(101), R, label="R")
n, = plt.plot(range(101), N, label="N")
plt.plot()
plt.legend()
plt.title("SEIR model with deaths from disease")

ax.margins(x=0)
axcolor = 'lightgoldenrodyellow'
axbeta = plt.axes([0.185, 0.16, 0.65, 0.03], facecolor=axcolor)
axgamma = plt.axes([0.185, 0.11, 0.65, 0.03], facecolor=axcolor)
axsigma = plt.axes([0.185, 0.06, 0.65, 0.03], facecolor=axcolor)
axdeath = plt.axes([0.185, 0.01, 0.65, 0.03], facecolor=axcolor)

sbeta = Slider(axbeta, 'beta', 0, 1, valinit=beta, valstep=0.01)
sgamma = Slider(axgamma, 'gamma', 0, 1, valinit=gamma, valstep=0.01)
ssigma = Slider(axsigma, 'sigma', 0, 1, valinit=sigma, valstep=0.01)
sdeath = Slider(axdeath, 'death', 0, 1, valinit=death, valstep=0.01)


def sli(value):
    bUp = sbeta.val
    gUp = sgamma.val
    sUp = ssigma.val
    dUp = sdeath.val

    S = [49]
    E = [0]
    I = [1]
    R = [0]
    for i in range(100):
        S.append(S[i]+dS(S[i], E[i], I[i], R[i], bUp, sUp, gUp))
        E.append(E[i]+dE(S[i], E[i], I[i], R[i], bUp, sUp, gUp))
        I.append(I[i]+dI(S[i], E[i], I[i], R[i], bUp, sUp, gUp, dUp))
        R.append(R[i]+dR(S[i], E[i], I[i], R[i], bUp, sUp, gUp))
    N = []
    for i in range(101):
        N.append(S[i]+E[i]+I[i]+R[i])
    s.set_ydata(S)
    e.set_ydata(E)
    ie.set_ydata(I)
    r.set_ydata(R)
    n.set_ydata(N)
    fig.canvas.draw_idle()


sbeta.on_changed(sli)
sgamma.on_changed(sli)
ssigma.on_changed(sli)
sdeath.on_changed(sli)

plt.show()
