import random
import inspect

### TASK It's Alive (i) ###
class Organism():
    ### TASK It's Alive (ii): size; division_threshold; uptake_rate; metabolic_rate; species (default ‘unknown’) ###
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, excretion_rate, species="unknown"):
        self.size = float(size) # Size (float)
        self.division_threshold = float(division_threshold) # Division threshold (float)
        self.original_uptake_rate = uptake_rate #####################################FOR VARIANT A
        self.uptake_rate = uptake_rate # Uptake rate (function)
        self.metabolic_rate = metabolic_rate # Metabolic rate (function)
        self.excretion_rate = excretion_rate ############################ presumably also a function
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
            excretion = self.excretion_rate(self.metabolic_rate(self.size))
            if self.size > self.division_threshold: #if size above division_threshold return True & uptake
                return True, float(uptake), float(excretion)
            else: # otherwise return True & uptake (presumably typing error & we should return False)
                return False, float(uptake), float(excretion)
        else: # if it's dead it can't divide & doesn't eat any food
            return "Dead", 0, 0


### TASK Hello World (i) ###
class Environment():
    ### TASK Hello World (ii): food; refill_rate; population ###
    def __init__(self, food, refill_rate, population):
        self.food = float(food) # food (float)
        self.refill_rate = float(refill_rate) # refill_rate (float)
        self.population = population # population (list of Organisms)
        self.accumulated_excretions = 0

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
            #####################################FOR VARIANT A
            func = inspect.getsource(organism.original_uptake_rate)
            func = func[func.find("lambda") + 6:]
            func = func[func.find("lambda") + 6:]
            func = func[func.find("lambda"):]
            func = func[: func.find(",")] + " * " + str((100 - self.accumulated_excretions/len(self.population)*10) / 100)
            new_uptake = eval(func)
            if new_uptake(organism.size) < 0: ################## Variant 1
                organism.uptake_rate = 0 ################### Variant 1
            else: ################## Variant 1
                organism.uptake_rate = new_uptake
            divide, eaten_food, excreted = organism.update(self.food) # Update the organism.
            self.food = self.food - eaten_food # Reduce food by the amount the organism ate.
            self.accumulated_excretions = self.accumulated_excretions + excreted

            if divide == "Dead": # If we want to remove dead ones
            # EASY VARIANT 2 - ALTHOUGH BORING RESULTS IF WE DO THIS ABSOLUTE, MAYBE FUNCTION BASED ON SIZE OR UPTAKE?
            # if divide = "Dead" or accumulated_excretions >= ...:
                continue
            elif divide: # If division True, remove organism from population & add 2 new instances (same parameters, size/2)
                size, division_threshold, original_uptake_rate, uptake_rate, metabolic_rate, excretion_rate, alive, species = list(organism.__dict__.values())
                new_organism_list.append(Organism(size/2, division_threshold, original_uptake_rate, metabolic_rate, excretion_rate, species))
                new_organism_list.append(Organism(size/2, division_threshold, original_uptake_rate, metabolic_rate, excretion_rate, species))
                no_of_divisions = no_of_divisions + 1
            else:
                new_organism_list.append(organism)

        self.population = new_organism_list
        self.food = self.food + self.refill_rate # After all organisms have been updated, increase food by refill_rate.

        # WE SHOULD PROBABLY REDUCE METABOLITES AT SOME POINT
        self.accumulated_excretions = self.accumulated_excretions * 0.9

        return no_of_divisions # Counts the total number of divisions that occur in an update cycle, and returns that value.





organism_active = Organism(100, 200, lambda x : 5, lambda x : 2, lambda x: 0.5*x, "active")
organism_passive = Organism(100, 200, lambda x : 4, lambda x : 1, lambda x: 0.5*x, "passive")

environment = Environment(10**3, 100, [organism_active, organism_passive])

res = []

for num in range(200):
    environment.update()
    act = 0
    pas = 0
    for x in environment.population:
        if x.species == "active":
            act += 1
        else:
            pas += 1
    res.append((len(environment.population), act, pas))


######
On the other hand, one could imagine that a given type of organism
could feed off the metabolite of another. This would mean creating two
species, one which lives off the byproducts of the other.

--> Instead of passing food we simply pass the byproduct for this species.
--> --> Maybe we can do something like A produces food (toxic for a) for B. B needs to eat this food because it's toxic for A
--> --> If there are too few A (maybe not all of A's food gets eaten) B dies --> We can make different uptakes until equilibrium
######
