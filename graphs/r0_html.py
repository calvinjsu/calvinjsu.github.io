import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, FloatSlider

# update funcs


def dS(S, I, N, beta):
    return -beta*S*I/N


def dE(S, E, I, N, beta, sigma):
    return beta*S*I/(N) - sigma*E


def dI(E, I, sigma, gamma, death):
    return sigma*E - gamma*I - death*I


def dR(I, gamma):
    return gamma*I


def plot(beta=0.75, sigma=0.25, gamma=0.33, death=0.01):
    x = np.arange(0, 101, 1)
    S, E, I, R, N = [990], [0], [10], [0], [1000]  # initial population
    for i in range(100):
        S.append(S[i] + dS(S[i], I[i], N[i], beta))
        E.append(E[i] + dE(S[i], E[i], I[i], N[i], beta, sigma))
        I.append(I[i] + dI(E[i], I[i], sigma, gamma, death))
        R.append(R[i] + dR(I[i], gamma))
        N.append(S[i]+E[i]+I[i]+R[i])
    plt.plot(x, S, label="S")
    plt.plot(x, E, label="E")
    plt.plot(x, I, label="I")
    plt.plot(x, R, label="R")
    plt.plot(x, N, label="N")
    plt.legend()
    plt.title(("R_0 = " + str(beta/gamma)[0:4]))


p = interact(plot, beta=(0, 1, 0.01), sigma=(0, 0.5, 0.01),
             gamma=(0, 0.5, 0.01), death=(0, 0.25, 0.01))
plt.show()
