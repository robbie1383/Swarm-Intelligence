from Particle import Particle


def distance(p1: Particle, p2: Particle):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


class PSO:

    def __init__(self, r, evaluation):
        self.particles = [Particle(r, evaluation) for i in range(10)]
        self.neighbourHoodSize = 3
        self.neighbours = []

    def updateNeighbours(self):
        # Compute all distances
        distances = []
        for i in self.particles:
            row = []
            for j in self.particles:
                row.append(distance(i, j))
            distances.append(row)

        # Find closest neighbours
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
            # Move based on PSO rules
            self.particles[particleIndex].move(self.particles[gbest], a)
