import numpy as np


class Particle:

    def __init__(self, r, evaluation):
        self.id = 0
        self.r = r
        self.maxv = 0.5
        self.x = np.random.uniform(-r, r)
        self.y = np.random.uniform(-r, r)
        self.v = [np.random.uniform(-self.maxv, self.maxv), np.random.uniform(-self.maxv, self.maxv)]
        self.f = evaluation(self.x, self.y)
        self.pbest = [self.x, self.y]
        self.evaluation = evaluation

    def updatePerformance(self):
        self.f = self.evaluation(self.x, self.y)
        if self.f < self.evaluation(self.pbest[0], self.pbest[1]):
            self.pbest = [self.x, self.y]

    def move(self, gbest, a):
        b = 2
        c = 2
        r = np.random.random()

        # Compute next velocity
        nextv = [a * self.v[0] + b * r * (self.pbest[0] - self.x) + c * r * (gbest.x - self.x),
                 a * self.v[1] + b * r * (self.pbest[1] - self.y) + c * r * (gbest.y - self.y)]
        nextv[0] = max(-self.maxv, min(self.maxv, nextv[0]))
        nextv[1] = max(-self.maxv, min(self.maxv, nextv[1]))

        # Compute next position
        self.x += nextv[0]
        self.y += nextv[1]
        self.v = nextv
