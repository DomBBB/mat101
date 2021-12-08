###
# Variant 1 & 3
###
###
# Variant 2 (killing of every organism at a threshold) would be rather boring,
# because it would result in one of two (obvious) scenarios:
# * Threshold is reached = All die (and it stays 0)
#     --> even when it's a function depending on the size
#    --> we would have the same boring result
# * Threshold is NOT reached = No organism dies
###
import random


class Organism():
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, excretion_rate, species="unknown"):
        self.size = float(size)
        self.division_threshold = float(division_threshold)
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.excretion_rate = excretion_rate
        self.species = species
        self.alive = True

    def update(self, accumulated_excretions, len_population, available_food=None):
        if self.alive:
            if available_food == None:
                uptake = self.uptake_rate(self.size)
            else:
                uptake = min(available_food, self.uptake_rate(self.size))
            self.size = self.size + uptake - accumulated_excretions/len_population/1000 - self.metabolic_rate(self.size) ##DOES THIS MAKE SENSE?
            excretion = self.excretion_rate(self.metabolic_rate(self.size))
            if self.size <= 0:
                self.alive = False
                return "Dead", float(uptake), float(excretion)
            if self.size > self.division_threshold:
                return True, float(uptake), float(excretion)
            else:
                return False, float(uptake), float(excretion)
        else:
            return "Dead", float(0), float(0)


class Environment():
    def __init__(self, food, refill_rate, population, reduce_metabolites):
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = population
        self.accumulated_excretions = 0
        self.reduce_metabolites = reduce_metabolites

    def update(self):
        random.shuffle(self.population)

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        no_of_divisions = 0
        new_organism_list = []

        # For each organism in the shuffled list
        for organism in self.population:
            # Update the organism
            if not organism.species == "excreter":
                divide, eaten_food, excreted = organism.update(self.accumulated_excretions, len(self.population), self.food)
                # Reduce food by the amount the organism ate.
                self.food = self.food - eaten_food
                self.accumulated_excretions = self.accumulated_excretions + excreted
            else:
                divide, eaten_food, excreted = organism.update(0, 1, self.accumulated_excretions)
                # Reduce metabolites by the amount the organism ate.
                self.accumulated_excretions = self.accumulated_excretions - eaten_food
            # We remove dead organisms
            if divide == "Dead":
                continue
            # If the organism returns the division signal True: Remove organism from population & add 2 new (same parameters, size/2)
            elif divide:
                size = organism.__dict__["size"]
                division_threshold = organism.__dict__["division_threshold"]
                uptake_rate = organism.__dict__["uptake_rate"]
                metabolic_rate = organism.__dict__["metabolic_rate"]
                excretion_rate = organism.__dict__["excretion_rate"]
                species = organism.__dict__["species"]
                new_organism_list.append(Organism(size/2, division_threshold, uptake_rate, metabolic_rate, excretion_rate, species))
                new_organism_list.append(Organism(size/2, division_threshold, uptake_rate, metabolic_rate, excretion_rate, species))
                no_of_divisions = no_of_divisions + 1
            else:
                new_organism_list.append(organism)

        self.population = new_organism_list
        # After all organisms have been updated, increase food by the refill_rate.
        self.food = self.food + self.refill_rate

        # Reduce metabolites at some point (environment discards a certain amount)
        self.accumulated_excretions = self.accumulated_excretions * self.reduce_metabolites

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        return no_of_divisions
