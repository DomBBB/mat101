import random
from basicOrganisms import Organism
class Environment():
    def __init__(self, food, refill_rate, population):
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = population

    def update(self):
        # Randomly shuffles a copy of the population list
            # AFTER shuffling we don't know the index in the original population:
        random.shuffle(self.population)

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        no_of_divisions = 0
        new_organism_list = []

        # For each organism in the shuffled list
        for organism in self.population:
            # Update the organism
            divide, eaten_food = organism.update(self.food)
            # Reduce food by the amount the organism ate.
            self.food = self.food - eaten_food

            # Not in task
                # If we want to remove dead organisms
            if divide == "Dead":
                continue
            # If the organism returns the division signal True: Remove organism from population & add 2 new (same parameters, size/2)
            elif divide:
                size, division_threshold, uptake_rate, metabolic_rate, alive, species = list(organism.__dict__.values())
                new_organism_list.append(Organism(size/2, division_threshold, uptake_rate, metabolic_rate, species))
                new_organism_list.append(Organism(size/2, division_threshold, uptake_rate, metabolic_rate, species))
                no_of_divisions = no_of_divisions + 1
            else:
                new_organism_list.append(organism)

        self.population = new_organism_list
        # After all organisms have been updated, increase food by the refill_rate.
        self.food = self.food + self.refill_rate

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        return no_of_divisions
