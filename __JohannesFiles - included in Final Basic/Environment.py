import random
from Organism import Organism


class Environment():
    def __init__(self, food, refill_rate, population,):
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = population
        self.DivNum = 0


    def update(self):
        shuffle_list = self.population.copy()
        random.shuffle(shuffle_list)



        for organism in shuffle_list:
            ready_to_divide, uptake = organism.update(self.food)
            self.food -= uptake

            if ready_to_divide:

                newOrganism = lambda organism: Organism(organism.size/2, organism.division_threshold, organism.uptake_rate, organism.metabolic_rate, organism.species)
                org1 = newOrganism(organism)
                org2 = newOrganism(organism)
                self.population.append(org1)
                self.population.append(org2)
                self.population.remove(organism)
                self.DivNum += 1


        self.food += self.refill_rate

        self.food = self.food + self.refill_rate
        print(f"Food: {self.food} units, no. divisions: {self.DivNum}, population: {len(self.population)}")





organism1 = Organism(100, 200, lambda x : 1/4 * x**(2/3), lambda x : 1/50 * x, "SizeGuys")
organism2 = Organism(100, 200, lambda x : 5, lambda x : 2, "SpecimentZero")

environment1 = Environment(10**3, 100, [organism1])


cap = 100

for round in range(0, cap):
    print(f"Round {round + 1}: ", end="")
    environment1.update()
