import numpy as np


class Particle:

    def __init__(self, range):
        self.id = 0
        self.x = np.random.uniform(-range, range)
        self.y = np.random.uniform(-range, range)
        self.v = np.random.rand(1, 2)
        self.f = 0
        self.gbest = 0, 0
        self.pbest = 0, 0
        self.neighbours = []
