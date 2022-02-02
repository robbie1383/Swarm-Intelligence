from matplotlib import pyplot as plt
import numpy as np
from PSO import PSO
import imageio
import os


def rosenbrock(x, y):
    a = 0
    b = 10
    return (a - x) ** 2 + b * (y - x ** 2) ** 2


def rastrigin(x, y):
    return 10 * 2 + (x ** 2 - 10 * np.cos(2 * np.pi * x)) + (y ** 2 - 10 * np.cos(2 * np.pi * y))


def plotFunction(range, evaluation):
    steps = 70
    x = np.linspace(-range, range, steps)
    y = np.linspace(-range, range, steps)
    z = np.array([evaluation(i, j) for j in y for i in x])

    X, Y = np.meshgrid(x, y)
    Z = z.reshape(steps, steps)

    plt.contourf(X, Y, Z, steps)
    plt.colorbar()


def findMinimum(r, evaluation, iterations):
    filenames = []
    particles = PSO(r, evaluation)

    # Plot starting points
    plotFunction(r, evaluation)
    for particle in particles.particles:
        plt.plot(particle.x, particle.y, 'wo')
    filename = f'start.png'
    filenames.append(filename)
    plt.savefig(filename)
    plt.close()

    a = 0.9
    step = (0.9 - 0.4)/iterations

    # Plot every iteration
    for iteration in range(iterations):
        plotFunction(r, evaluation)
        particles.move(a)
        for particle in particles.particles:
            plt.plot(particle.x, particle.y, 'wo')
        filename = f'{iteration}.png'
        filenames.append(filename)
        plt.savefig(filename)
        plt.close()
        a -= step

    return filenames


def main():
    # Create pictures of every iteration
    filenames = findMinimum(5, rastrigin, 20)

    # Create GIF
    with imageio.get_writer('POS.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)

    # Remove files
    for filename in set(filenames):
        os.remove(filename)


if __name__ == '__main__':
    main()

