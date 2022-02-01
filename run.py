from matplotlib import pyplot as plt
import numpy as np
from PSO import PSO

def rosenbrock(x, y):
    a = 0
    b = 10
    return (a - x)**2 + b*(y - x**2)**2

def rastrigin(x, y):
    return 10*2 + (x**2 - 10*np.cos(2*np.pi*x)) + (y**2 - 10*np.cos(2*np.pi*y))

def plotRosenbrock(range):
    steps = 70
    x = np.linspace(-range, range, steps)
    y = np.linspace(-range, range, steps)
    z = np.array([rosenbrock(i, j) for j in y for i in x])

    X, Y = np.meshgrid(x, y)
    Z = z.reshape(steps, steps)

    plt.contourf(X, Y, Z, steps)
    plt.colorbar()

def plotRastrigin(range):
    steps = 70
    x = np.linspace(-range, range, steps)
    y = np.linspace(-range, range, steps)
    z = np.array([rastrigin(i, j) for j in y for i in x])

    X, Y = np.meshgrid(x, y)
    Z = z.reshape(steps, steps)

    plt.contourf(X, Y, Z, steps)
    plt.colorbar()

def main():
    range = 5
    particles = PSO(range)
    plotRosenbrock(range)
    for particle in particles.particles:
        plt.plot(particle.x, particle.y, 'wo')
    plt.show()


if __name__ == '__main__':
    main()