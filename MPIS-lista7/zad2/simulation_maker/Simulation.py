import random


class Simulation:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.bins = [0] * n
        self.Ln = 0
        self.counter = 1

    def shouldStopSimulation(self):
        return self.counter == self.n

    def make_throw(self):
        possible_bins = []
        for _ in range(self.d):
            possible_bins.append(random.randint(0, self.n-1))
        min_balls = min([self.bins[x] for x in possible_bins])
        throw_to = 0
        for trash in possible_bins:
            if min_balls == self.bins[trash]:
                throw_to = trash
                break
        self.bins[throw_to] += 1

    def run(self):
        while not self.shouldStopSimulation():
            self.make_throw()
            self.counter += 1
        self.getLn()  # after n balls

    def getLn(self):
        self.Ln = max(self.bins)


if __name__ == "__main__":
    simulation = Simulation(30000, 2)
    simulation.run()
