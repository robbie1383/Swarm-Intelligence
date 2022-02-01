from matplotlib import pyplot as plt
import numpy as np

def rosenbrock(x, y):
    a = 0
    b = 10
    return (a - x)**2 + b*(y - x**2)**2

def rastrigin(x, y):
    return 10*2 + (x**2 - 10*np.cos(2*np.pi*x)) + (y**2 - 10*np.cos(2*np.pi*y))

def plotRosenbrock():
    steps = 70
    x = np.linspace(-2, 2, steps)
    y = np.linspace(-1, 3, steps)
    z = np.array([rosenbrock(i, j) for j in y for i in x])

    X, Y = np.meshgrid(x, y)
    Z = z.reshape(steps, steps)

    plt.contourf(X, Y, Z, steps)
    plt.colorbar()

def plotRastrigin():
    steps = 70
    x = np.linspace(-5, 5, steps)
    y = np.linspace(-5, 5, steps)
    z = np.array([rastrigin(i, j) for j in y for i in x])

    X, Y = np.meshgrid(x, y)
    Z = z.reshape(steps, steps)

    plt.contourf(X, Y, Z, steps)
    plt.colorbar()

def main():
    plotRosenbrock()
    plt.show()
    plotRastrigin()

if __name__ == '__main__':
    main()