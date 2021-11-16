import random
import matplotlib.pyplot as plt

class Organism():
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, species="unknown"):
        self.size = float(size)
        self.division_threshold = float(division_threshold)
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.alive = True
        self.species = species

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
            return "Dead", 0



class Environment():
    def __init__(self, food, refill_rate, population):
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = population
        self.gene_pool = []

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
            # If the organism returns the division signal True: Remove organism from population & add 2 new (same parameters, size/2)
            elif divide:
                size, division_threshold, uptake_rate, metabolic_rate, alive, species = list(organism.__dict__.values())
                self.gene_pool.append([division_threshold, uptake_rate, metabolic_rate])
                uptake_rate = self.gene_pool[(random.randrange(0,len(self.gene_pool)))][1]
                metabolic_rate = self.gene_pool[(random.randrange(0,len(self.gene_pool)))][2]
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


organism_active = Organism(100, 200, lambda x : 5, lambda x : 2, "active")
organism_passive = Organism(100, 200, lambda x : 4, lambda x : 1, "passive")

# CHANGE THESE TO MAKE OTHER TESTS
environment = Environment(10**3, 1000, [organism_active, organism_passive])

res = []
for num in range(5*10**3):
    environment.update()
    active = 0
    passive = 0
    attributes = {"up_active": 0, "up_passive": 0, "me_active": 0, "me_passive": 0}
    for organism in environment.population:
        if organism.species == "active":
            active += 1
        else:
            passive += 1
        if organism.uptake_rate(0) == 5:
            attributes["up_active"] = attributes["up_active"] + 1
        else:
            attributes["up_passive"] = attributes["up_passive"] + 1
        if organism.metabolic_rate(0) == 2:
            attributes["me_active"] = attributes["me_active"] + 1
        else:
            attributes["me_passive"] = attributes["me_passive"] + 1
    res.append((num+1, len(environment.population), active, passive, attributes))

idx_ls = []
pop_ls = []
act_ls = []
pas_ls = []
up_ac = []
up_pa = []
me_ac = []
me_pa = []
for item in res:
    idx_ls.append(item[0])
    pop_ls.append(item[1])
    act_ls.append(item[2])
    pas_ls.append(item[3])
    up_ac.append(item[4]["up_active"])
    up_pa.append(item[4]["up_passive"])
    me_ac.append(item[4]["me_active"])
    me_pa.append(item[4]["me_passive"])

plt.plot(idx_ls, pop_ls)
plt.plot(idx_ls, act_ls)
plt.plot(idx_ls, pas_ls)
plt.show()

plt.plot(idx_ls, up_ac)
plt.plot(idx_ls, up_pa)
plt.plot(idx_ls, me_ac)
plt.plot(idx_ls, me_pa)
plt.show()