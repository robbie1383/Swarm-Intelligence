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
    steps = 35
    x = np.linspace(-range, range, steps)
    y = np.linspace(-range, range, steps)
    z = np.array([evaluation(i, j) for j in y for i in x])

    X, Y = np.meshgrid(x, y)
    Z = z.reshape(steps, steps)

    plt.contourf(X, Y, Z, steps)
    plt.colorbar()


def findMinimum(r, evaluation, iterations, function_name, neighbourHoodSize, particle_num):
    filenames = []
    particles = PSO(r, evaluation, neighbourHoodSize, particle_num)

    # Plot starting points
    plotFunction(r, evaluation)
    for particle in particles.particles:
        plt.plot(particle.x, particle.y, 'wo')
    filename = f'{function_name}start.png'
    filenames.append(filename)
    plt.savefig(filename)
    plt.close()

    a = 0.2
    step = (0.9 - 0.4) / iterations

    # Plot every iteration
    for iteration in range(iterations):
        plotFunction(r, evaluation)
        particles.move(a)
        for particle in particles.particles:
            plt.plot(particle.x, particle.y, 'wo')
        filename = f'{function_name}_{iteration}.png'
        filenames.append(filename)
        plt.savefig(filename)
        plt.close()
        a -= step

    return filenames


def main():
    range = 5
    iterations = 20
    particles = 10
    neighbours = 5

    # Create pictures of every iteration
    filenames_rosenbrock = findMinimum(range, rosenbrock, iterations, "rosenbrock", neighbours, particles)
    filenames_rastrigin = findMinimum(range, rastrigin, iterations, "rastrigin", neighbours, particles)

    # Create GIF
    rosenbrock_gif_name = f'rosenbrock_{range}_{iterations}_{particles}_{neighbours}.gif'
    with imageio.get_writer(rosenbrock_gif_name, mode='I') as writer:
        for filename in filenames_rosenbrock:
            image = imageio.imread(filename)
            writer.append_data(image)

    rastrigin_gif_name = f'rastrigin_{range}_{iterations}_{particles}_{neighbours}.gif'
    with imageio.get_writer(rastrigin_gif_name, mode='I') as writer:
        for filename in filenames_rastrigin:
            image = imageio.imread(filename)
            writer.append_data(image)
    # Remove files
    # for filename in set(filenames_rastrigin):
    #     os.remove(filename)
    #
    # for filename in set(filenames_rosenbrock):
    #     os.remove(filename)


if __name__ == '__main__':
    main()
