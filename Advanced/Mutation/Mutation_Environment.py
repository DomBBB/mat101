import random
from Organism import Organism

class MEnvironment():
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
