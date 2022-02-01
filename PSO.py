import numpy as np

class PSO:

    def __init__(self, r):
        self.particles = [Particle(r) for i in range(20)]
        self.neighbourHoodSize = 3


class Particle:

    def __init__(self, range):
        self.x = np.random.uniform(-range, range)
        self.y = np.random.uniform(-range, range)
        self.v = np.random.rand(1,2)
        self.f = 0