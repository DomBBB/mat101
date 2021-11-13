import random

### TASK It's Alive (i) ###
class Organism():
    ### TASK It's Alive (ii): size; division_threshold; uptake_rate; metabolic_rate; species (default ‘unknown’) ###
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, species="unknown"):
        self.size = float(size) # Size (float)
        self.division_threshold = float(division_threshold) # Division threshold (float)
        self.uptake_rate = uptake_rate # Uptake rate (function)
        self.metabolic_rate = metabolic_rate # Metabolic rate (function)
        self.alive = True # Alive (bool)
        self.species = species  # Species name (string)

    ### TASK It's Alive (iv): If no value for available_food, uptake should be uptake rate of the organism. ###
    def update(self, available_food=None):
        if self.alive:
            if available_food == None:
                uptake = self.uptake_rate(self.size)
            else:
                uptake = min(available_food, self.uptake_rate(self.size)) # set var uptake to min of available_food and uptake_rate
            self.size = self.size + uptake - self.metabolic_rate(self.size) # if alive: size += uptake & size -= metabolic_rate
            if self.size <= 0:
                self.alive = False
            if self.size > self.division_threshold: #if size above division_threshold return True & uptake
                return True, float(uptake)
            else: # otherwise return True & uptake (presumably typing error & we should return False)
                return False, float(uptake)
        else: # if it's dead it can't divide & doesn't eat any food
            return "Dead", 0


### TASK Hello World (i) ###
class Environment():
    ### TASK Hello World (ii): food; refill_rate; population ###
    def __init__(self, food, refill_rate, population):
        self.food = float(food) # food (float)
        self.refill_rate = float(refill_rate) # refill_rate (float)
        self.population = population # population (list of Organisms)

    ### TASK Hello World (iii) ###
    def update(self):
        ###
        # AFTER shuffling we don't know the index in the original population:
        # --> WHY do we copy? Shouldn't we replace the population with the new population?
        # --> --> Do we remove dead ones?
        ###
        shuffle_list = self.population.copy() # UNNECESSARY???
        random.shuffle(shuffle_list) # Randomly shuffles a copy of the population list (shuffle method in random library)

        no_of_divisions = 0 # Counts the total number of divisions that occur in an update cycle, and returns that value.
        new_organism_list = []

        for organism in shuffle_list: # For each organism in the shuffled list:
            divide, eaten_food = organism.update(self.food) # Update the organism.
            self.food = self.food - eaten_food # Reduce food by the amount the organism ate.

            if divide == "Dead": # If we want to remove dead ones
                continue
            elif divide: # If division True, remove organism from population & add 2 new instances (same parameters, size/2)
                size, division_threshold, uptake_rate, metabolic_rate, alive, species = list(organism.__dict__.values())
                new_organism_list.append(Organism(size/2, division_threshold, uptake_rate, metabolic_rate, species))
                new_organism_list.append(Organism(size/2, division_threshold, uptake_rate, metabolic_rate, species))
                no_of_divisions = no_of_divisions + 1
            else:
                new_organism_list.append(organism)

        self.population = new_organism_list
        self.food = self.food + self.refill_rate # After all organisms have been updated, increase food by refill_rate.

        return no_of_divisions # Counts the total number of divisions that occur in an update cycle, and returns that value.
