import matplotlib.pyplot as plt
import numpy as np

def logistic(gamma, x, n):
    for i in range(n):
        x = gamma*x*(1-x)
    return x

# Quadratic causes overflow
# def quadratic(gamma, x, n):
#     for i in range(n):
#         x = gamma - x**2
#     return x

def getCycles(gamma, x, cycles, func):
    for i in range(cycles):
        x = np.vstack((x[0:max(1, i), :], func(gamma, x[max(0, i-1), :], 1)))
    return x

steps = 2000
cycles = 512
gamma_min, gamma_max = 2.97, 4.0
alpha = 0.02

gamma = np.linspace(gamma_min, gamma_max, steps)
x = np.full((1, steps), 0.5)

# Get one stable population value
x = logistic(gamma, x, 1000)
# Get <cycles> possible values
x = getCycles(gamma, x, cycles, logistic)

gamma = np.repeat(gamma.reshape((-1, 1)).T, cycles, axis=0)

plt.scatter(gamma, x, s=1, alpha=alpha)
plt.title('Feigenbaum Bifurcation Graph')
plt.xlabel('gamma (Fertility)')
plt.ylabel('Stable Population')
plt.axis([gamma_min, gamma_max, 0, 1])
plt.show()