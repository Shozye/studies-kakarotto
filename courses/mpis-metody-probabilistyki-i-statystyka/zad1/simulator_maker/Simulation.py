import random
from utils import init_answers


class Simulation:
    def __init__(self, n):
        self.n = n
        self.bins = [0] * n
        self.answers = init_answers()
        self.isBnSet, self.isCnSet = False, False
        self.distribution = [n, 0, 0]  # on 2 there is amount of bins with 2 or more balls
        self.counter = 1

    def shouldStopSimulation(self):
        return (self.distribution[0] + self.distribution[1]) == 0

    def run(self):
        while not self.shouldStopSimulation():
            random_bin_to_throw_ball = random.randint(0, self.n - 1)
            self.bins[random_bin_to_throw_ball] += 1

            if self.bins[random_bin_to_throw_ball] <= 2:
                self.distribution[self.bins[random_bin_to_throw_ball] - 1] -= 1
                self.distribution[self.bins[random_bin_to_throw_ball]] += 1

            if self.distribution[2] == 1 and not self.isBnSet:  # jezeli pierwszy raz mamy dwie kule w tym samym koszu
                self.getBn()

            if self.counter == self.n:  # po n rzutach
                self.getUn()
                self.getLn()

            if self.distribution[0] == 0 and not self.isCnSet:  # gdy nie mamy pustego kosza
                self.getCn()

            self.counter += 1
        self.getDn()  # gdy w kazdym koszu mamy 2 kule
        self.getDn__Minus__Cn()

    def getBn(self):
        self.answers["Bn"] = self.counter
        self.isBnSet = True

    def getDn__Minus__Cn(self):
        self.answers["Dn__Minus__Cn"] = self.answers["Dn"] - self.answers["Cn"]

    def getDn(self):
        self.answers["Dn"] = self.counter

    def getCn(self):
        self.answers["Cn"] = self.counter
        self.isCnSet = True

    def getLn(self):
        self.answers["Ln"] = max(self.bins)

    def getUn(self):
        self.answers["Un"] = self.distribution[0]


if __name__ == "__main__":
    simulation = Simulation(30000)
    simulation.run()
