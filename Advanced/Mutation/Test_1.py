import random


class Organism:
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, species="unknown"):
        self.size = float(size)
        self.division_threshold = float(division_threshold)
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.alive = True
        self.species = species

    def update(self, available_food=None):
        if available_food == None:
            uptake = self.uptake_rate(self.size)
        else:
            uptake = min(available_food, self.uptake_rate(self.size))
        if self.alive:
            self.size += uptake - self.metabolic_rate(self.size)
            if self.size <= 0:
                self.alive = False
                return False, float(uptake)
            if self.size >= self.division_threshold:
                return True, float(uptake)
            else:
                return False, float(uptake)
        else:
            return False, uptake

class Environment():
    def __init__(self, food, refill_rate, population, MutPopulation):
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = population
        self.DivNum = 0
        self.MutPopulation = MutPopulation
        self.MutNum = 0

    def update(self):
        shuffle_list = self.population.copy()
        random.shuffle(shuffle_list)

        no_of_divisions = 0
        no_of_Mutations = 0
        Mutated_Organism_list = []

        for organism in shuffle_list:
            ready_to_divide, uptake = organism.update(self.food)
            self.food -= uptake

            if ready_to_divide:

                Mutation_Chance = random.randint(1, 5)

                if Mutation_Chance == 3:
                    newOrganism = lambda organism: Organism(organism.size/2 + random.random()*10-5, organism.division_threshold + random.random()*10-5, organism.uptake_rate, organism.metabolic_rate, organism.species)
                    org1 = newOrganism(organism)
                    org2 = newOrganism(organism)
                    self.population.append(org1)
                    self.population.append(org2)
                    self.population.remove(organism)
                    self.MutPopulation.append(org1)
                    self.MutPopulation.append(org2)
                    self.DivNum += 1
                    no_of_Mutations += 1
                    self.MutNum += 1



                else:
                    newOrganism = lambda organism: Organism(organism.size/2, organism.division_threshold, organism.uptake_rate, organism.metabolic_rate, organism.species)
                    org1 = newOrganism(organism)
                    org2 = newOrganism(organism)
                    self.population.append(org1)
                    self.population.append(org2)
                    self.population.remove(organism)
                    self.DivNum += 1


        self.food += self.refill_rate

        self.food = self.food + self.refill_rate
        print(f"Food: {self.food} units, no. divisions: {self.DivNum}, population: {len(self.population)}, no. Mutation: {self.MutNum}, Mutations: {len(self.MutPopulation)}")





organism1 = Organism(100, 200, lambda x : 1/4 * x**(2/3), lambda x : 1/50 * x, "SizeGuys")
organism2 = Organism(100, 200, lambda x : 5, lambda x : 2, "SpecimentZero")

environment1 = Environment(10**3, 100, [organism1], [])


cap = 100

for round in range(0, cap):
    print(f"Round {round + 1}: ", end="")
    environment1.update()
