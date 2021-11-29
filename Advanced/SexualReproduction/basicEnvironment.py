import random
from basicOrganisms import Organism

class Environment():
    def __init__(self, food, refill_rate, population):
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = list(population)

    def update(self):
        # Randomly shuffles a copy of the population list
            # AFTER shuffling we don't know the index in the original population:
            # --> WHY do we copy? Shouldn't we replace the population with the new population?
            # --> --> Do we remove dead ones?
        shuffle_list = self.population.copy()
        random.shuffle(shuffle_list)

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        no_of_divisions = 0
        new_organism_list = []

        # For each organism in the shuffled list
        for organism in shuffle_list:
            # Update the organism
            divide, eaten_food = organism.update(self.food)
            # Reduce food by the amount the organism ate.
            self.food = self.food - eaten_food

            # Not in task
                # If we want to remove dead organisms
            if divide == "Dead":
                continue
            # If the organism returns the division signal True: Create New Organisms
            elif divide:
                size = organism.__dict__["size"]
                fertility_threshold = organism.__dict__["fertility_threshold"]
                uptake_rate = organism.__dict__["uptake_rate"]
                metabolic_rate = organism.__dict__["metabolic_rate"]
                species = organism.__dict__["species"]
                new_organism_list.append(Organism(size/2, fertility_threshold, uptake_rate, metabolic_rate, species))
                new_organism_list.append(Organism(size/2, fertility_threshold, uptake_rate, metabolic_rate, species))
                no_of_divisions = no_of_divisions + 1
            else:
                new_organism_list.append(organism)

        self.population = new_organism_list
        # After all organisms have been updated, increase food by the refill_rate.
        self.food = self.food + self.refill_rate

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        return no_of_divisions
