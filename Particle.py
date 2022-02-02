import numpy as np


class Particle:

    def __init__(self, r, evaluation):
        self.id = 0
        self.x = np.random.uniform(-r, r)
        self.y = np.random.uniform(-r, r)
        self.v = [np.random.uniform(-r, r),np.random.uniform(-r, r)]
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
        nextv = [a * self.v[0] + b * r * (self.pbest[0] - self.x) + c * r * (gbest.x - self.x), a * self.v[1] + b * r * (self.pbest[1] - self.y) + c * r * (gbest.y - self.y)]
        if nextv[0] < -r : nextv[0] = -r
        if nextv[1] < -r: nextv[1] = -r
        if nextv[0] > r : nextv[0] = r
        if nextv[1] > r: nextv[1] = r
        self.x += nextv[0]
        self.y += nextv[1]
        self.v = nextv