from Particle import Particle


class PSO:

    def __init__(self, r):
        self.particles = []
        for i in range(20):
            p = Particle()
            p.id = i
            self.particles.append(p)
        self.neighbourHoodSize = 3

    def update_neighbours(self):
        for p1 in self.particles:
            long = 0
            if len(p1.neighbours):
                for n in p1.neighbours:
                    if self.distance(p1, n) > long:
                        long = self.distance(p1, n)
            for p2 in self.particles:
                if p1.id != p2.id:
                    if self.distance(p1, p2) < long:
                        p1.neighbours.pop()
                        p1.neighbours.append(p2)

    def distance(self, p1: Particle, p2: Particle):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
