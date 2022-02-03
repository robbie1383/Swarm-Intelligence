import os

import imageio
import matplotlib.pyplot as plt
import sympy as symp
import numpy as np


def rosenbrock(x, y):
    a = 0
    b = 10
    return (a - x) ** 2 + b * (y - x ** 2) ** 2


'''
Parameter of rastrigin:
- fc: refers to whether we want to use library sympy or numpy to define cos and pi
=>library sympy will be used to compute the derivates
=>library numpy will be used to plot the function. Even though sympy provides plot, sympy doesn't provide dot plot which 
is useful to see how GD iterations. That's why numpy will be used
'''


def rastrigin(x, y, fc):
    return 10 * 2 + (x ** 2 - 10 * fc.cos(2 * fc.pi * x)) + (y ** 2 - 10 * fc.cos(2 * fc.pi * y))


'''
var1: represent which variable will be differentiated
value1: corresponding value for var 1
var1: represent which variable will not be differentiated
value1: corresponding value for var 2
'''


def derivatives(function, var1, var2, value1, value2):
    der = symp.diff(function, var1)
    return der.doit().subs({var1: value1, var2: value2})


def findMinimum(function):
    x = symp.Symbol('x')  # To define a function with the library "sympy", you need to define all the variable as symbol
    y = symp.Symbol('y')  # same
    eps = 0.001  # precision to find the minima of the function
    maxIter = 100  # max number of interation
    # init_x = 0.8  # initial x to start GD
    # init_y = 0.6  # initial y to start BD
    init_x = np.random.uniform(-5, 5)
    init_y = np.random.uniform(-5, 5)
    z = function.subs({x: init_x, y: init_y})  # f(x,y) with initial values
    alpha = 0.001  # Learning rate
    condition = 3  # initial condition that will be updated. To stop GD, condition <eps
    iter = 0
    new_z = z
    filenames = []
    while condition > eps and iter < maxIter:
        plt.scatter(init_x, init_y)
        new_x = init_x - alpha * derivatives(function, x, y, init_x, init_y)
        new_y = init_y - alpha * derivatives(function, y, x, init_y, init_x)

        init_x = new_x
        init_y = new_y

        z = function.subs({x: init_x, y: init_y})
        condition = abs(new_z - z)

        new_z = z
        iter = iter + 1

        filename = f'{iter}.png'
        filenames.append(filename)
        plt.savefig(filename)
        print("x=", round(init_x, 3), "y=", round(init_y, 3), "condition=", round(condition, 3))
    # plt.show()
    print("x=", round(init_x, 3), "y=", round(init_y, 3), "condition=", round(condition, 3))
    return filenames


def plott(function):
    if function == rosenbrock:
        steps = 70
        x = np.linspace(-5, 5, steps)
        y = np.linspace(-5, 5, steps)
        z = np.array([function(i, j) for j in y for i in x])

        X, Y = np.meshgrid(x, y)
        Z = z.reshape(steps, steps)

        plt.contourf(X, Y, Z, steps)
        plt.colorbar()
    else:
        steps = 70
        x = np.linspace(-5, 5, steps)
        y = np.linspace(-5, 5, steps)
        z = np.array([function(i, j, np) for j in y for i in x])

        X, Y = np.meshgrid(x, y)
        Z = z.reshape(steps, steps)

        plt.contourf(X, Y, Z, steps)
        plt.colorbar()


def main():
    function = rosenbrock  # Function we decide to run GD on
    plott(function)
    x = symp.Symbol('x')
    y = symp.Symbol('y')
    # filenames = findMinimum(function(x, y, symp))
    filenames = findMinimum(function(x, y))
    # Create GIF
    with imageio.get_writer('Gradient.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)

    # Remove files
    for filename in set(filenames):
        os.remove(filename)


if __name__ == '__main__':
    main()
