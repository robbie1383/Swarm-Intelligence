from Particle import Particle

def distance(p1: Particle, p2: Particle):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

class PSO:

    def __init__(self, r, evaluation):
        self.particles = [Particle(r, evaluation) for i in range(10)]
        self.neighbourHoodSize = 3
        self.neighbours = []

    def updateNeighbours(self):
        distances = []
        for i in self.particles:
            row = []
            for j in self.particles:
                row.append(distance(i, j))
            distances.append(row)

        for i in range(len(self.particles)):
            toAll = distances[i].copy()
            toAll.sort()
            toAll = toAll[1:len(toAll)]
            self.neighbours.append([distances[i].index(toAll[j]) for j in range(self.neighbourHoodSize)])

    def move(self, a):
        self.updateNeighbours()
        # Update performance
        for particle in self.particles:
            particle.updatePerformance()
        # Move towards minimum
        for particleIndex in range(len(self.particles)):
            # Find neighbour gbest
            gbest = self.neighbours[particleIndex][0]
            for i in range(1, self.neighbourHoodSize):
                if self.particles[self.neighbours[particleIndex][i]].f < self.particles[gbest].f:
                    gbest = self.neighbours[particleIndex][i]
            # Move
            self.particles[particleIndex].move(self.particles[gbest], a)

"""
This one gives errors and i can't really figure out what you did so I don't really know how to fix it
    def updateNeighbours(self):
        for i in range(len(self.particles)):  # find neighbours for each Particle i
            longest = 0
            for j in range(len(self.particles)):  # compare each neighbour j distance to i
                if i != j:
                    if len(self.neighbours) >= i:  # already have neighbours
                        for p in self.neighbours[i]:
                            if self.distance(self.particles[i], p) > longest:
                                longest = self.distance(self.particles[i], p)
                        if (self.distance(self.particles[i], self.particles[j])) < longest:
                            self.neighbours[i].pop()
                            self.neighbours[i].append(j)  # update longest neighbour
                            longest = self.distance(self.particles[i], self.particles[j])
                    else:  # first time run, no neighbours
                        if self.distance(self.particles[i], self.distance(self.particles[j])) > longest:
                            longest = self.distance(self.particles[i], p)
                            self.neighbours[i].append(j)
"""
