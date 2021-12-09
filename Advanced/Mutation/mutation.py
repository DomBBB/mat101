import random


class Organism():
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, species="unknown"):
        self.size = float(size)
        self.division_threshold = float(division_threshold)
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.species = species
        self.alive = True

    def update(self, available_food=None):
        if self.alive:
            if available_food == None:
                uptake = self.uptake_rate(self.size)
            else:
                uptake = min(available_food, self.uptake_rate(self.size))
            self.size = self.size + uptake - self.metabolic_rate(self.size)
            if self.size <= 0:
                self.alive = False
                return "Dead", float(uptake)
            if self.size > self.division_threshold:
                return True, float(uptake)
            else:
                return False, float(uptake)
        else:
            return "Dead", float(0)


class Environment():
    def __init__(self, food, refill_rate, population, mut_population):
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = population
        self.mut_population = mut_population

    def update(self):
        random.shuffle(self.population)

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        no_of_divisions = 0
        new_organism_list = []
        no_of_mutations = 0
        mut_organism_list = []

        # For each organism in the shuffled list
        for organism in self.population:
            # Update the organism
            divide, eaten_food = organism.update(self.food)
            # Reduce food by the amount the organism ate.
            self.food = self.food - eaten_food
            # We remove dead organisms
            if divide == "Dead":
                continue
            # If the organism returns the division signal True:...
            elif divide:
                mutation_chance = random.randint(1, 5)

                size = organism.__dict__["size"]
                division_threshold = organism.__dict__["division_threshold"]
                uptake_rate = organism.__dict__["uptake_rate"]
                metabolic_rate = organism.__dict__["metabolic_rate"]
                species = organism.__dict__["species"]

                if mutation_chance < 3:
                    new_org1 = Organism(size/2 + random.random()*10-5, division_threshold + random.random()*10-5, uptake_rate, metabolic_rate, species)
                    new_org2 = Organism(size/2 + random.random()*10-5, division_threshold + random.random()*10-5, uptake_rate, metabolic_rate, species)
                    new_organism_list.append(new_org1)
                    new_organism_list.append(new_org2)
                    mut_organism_list.append(new_org1)
                    mut_organism_list.append(new_org2)
                    no_of_divisions = no_of_divisions + 1
                    no_of_mutations = no_of_mutations + 1
                else:
                    new_org1 = Organism(size/2, division_threshold, uptake_rate, metabolic_rate, species)
                    new_org2 = Organism(size/2, division_threshold, uptake_rate, metabolic_rate, species)
                    new_organism_list.append(new_org1)
                    new_organism_list.append(new_org2)
                    if organism in mut_organism_list:
                        mut_organism_list.append(new_org1)
                        mut_organism_list.append(new_org2)
                    no_of_divisions = no_of_divisions + 1
            else:
                new_organism_list.append(organism)

        self.population = new_organism_list
        self.mut_population.extend(mut_organism_list)
        self.mut_population = list(set(self.mut_population))
        # After all organisms have been updated, increase food by the refill_rate.
        self.food = self.food + self.refill_rate

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        return no_of_divisions, no_of_mutations
