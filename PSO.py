from Particle import Particle


class PSO:

    def __init__(self, r):
        self.particles = [Particle(r) for i in range(20)]
        self.neighbourHoodSize = 3
        self.neighbours = []

    def update_neighbours(self):
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

    def distance(self, p1: Particle, p2: Particle):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
