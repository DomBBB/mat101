import matplotlib.pyplot as plt
import random

class Organism():
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, species="unknown", origin=None):
        self.size = float(size)
        self.division_threshold = float(division_threshold)
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.alive = True
        self.species = species
        self.origin = origin

    def update(self, available_food = None):
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
    def __init__(self, food, refill_rate, population, env):
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = population
        self.env = env

    def update(self):
        # Randomly shuffles a copy of the population list
            # AFTER shuffling we don't know the index in the original population:
        random.shuffle(self.population)

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        no_of_divisions = 0
        new_organism_list = []

        # For each organism in the shuffled list
        for organism in self.population:
            if organism.origin == None:
                organism.origin = self.env
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
                size = organism.__dict__["size"]
                division_threshold = organism.__dict__["division_threshold"]
                uptake_rate = organism.__dict__["uptake_rate"]
                metabolic_rate = organism.__dict__["metabolic_rate"]
                species = organism.__dict__["species"]
                origin = organism.__dict__["origin"]
                new_organism_list.append(Organism(size/2, division_threshold, uptake_rate, metabolic_rate, species, origin))
                new_organism_list.append(Organism(size/2, division_threshold, uptake_rate, metabolic_rate, species, origin))
                no_of_divisions = no_of_divisions + 1
            else:
                new_organism_list.append(organism)

        self.population = new_organism_list
        # After all organisms have been updated, increase food by the refill_rate.
        self.food = self.food + self.refill_rate

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        return no_of_divisions


    def migrate(self, own_pop, new_pop):
        self.population = own_pop + new_pop


# CHANGE THESE (RATES) TO MAKE OTHER TESTS
organism_active1 = Organism(100, 200, lambda x : 5, lambda x : 2, "active")
organism_passive1 = Organism(100, 200, lambda x : 4, lambda x : 1, "passive")

# CHANGE THESE TO MAKE OTHER TESTS
environment1 = Environment(0, 100, [organism_passive1], "env1")


# CHANGE THESE (RATES) TO MAKE OTHER TESTS
organism_active2 = Organism(100, 200, lambda x : 5, lambda x : 2, "active")
organism_passive2 = Organism(100, 200, lambda x : 4, lambda x : 1, "passive")

# CHANGE THESE TO MAKE OTHER TESTS
environment2 = Environment(10**3, 1000,  [organism_active2, organism_passive2], "env2")

res1 = []
res2 = []
for num in range(2*10**3):
    environment1.update()
    environment2.update()
    if num%1000 == 0:
        env1pop = sorted(environment1.population, key=lambda x: x.size, reverse=True)
        env2pop = sorted(environment2.population, key=lambda x: x.size, reverse=True)
        if len(env1pop) >= 10 and len(env2pop) >= 10:
            environment1.migrate(env1pop[len(env1pop)//10:], env2pop[:len(env2pop)//10])
            environment2.migrate(env2pop[len(env2pop)//10:], env1pop[:len(env1pop)//10])

    active1 = 0
    passive1 = 0
    env11 = 0
    env21 = 0
    for organism in environment1.population:
        if organism.species == "active":
            active1 += 1
        else:
            passive1 += 1
        if organism.origin == "env1":
            env11 += 1
        else:
            env21 += 1
    res1.append((num+1, len(environment1.population), active1, passive1, env11, env21))

    active2 = 0
    passive2 = 0
    env12 = 0
    env22 = 0
    for organism in environment2.population:
        if organism.species == "active":
            active2 += 1
        else:
            passive2 += 1
        if organism.origin == "env1":
            env12 += 1
        else:
            env22 += 1
    res2.append((num+1, len(environment2.population), active2, passive2, env12, env22))


idx_ls1 = []
pop_ls1 = []
act_ls1 = []
pas_ls1 = []
env1_ls1 = []
env2_ls1 = []
for item in res1:
    idx_ls1.append(item[0])
    pop_ls1.append(item[1])
    act_ls1.append(item[2])
    pas_ls1.append(item[3])
    env1_ls1.append(item[4])
    env2_ls1.append(item[5])
plt.plot(idx_ls1, pop_ls1)
plt.plot(idx_ls1, act_ls1)
plt.plot(idx_ls1, pas_ls1)
plt.plot(idx_ls1, env1_ls1)
plt.plot(idx_ls1, env2_ls1)
plt.show()



idx_ls2 = []
pop_ls2 = []
act_ls2 = []
pas_ls2 = []
env1_ls2 = []
env2_ls2 = []
for item in res2:
    idx_ls2.append(item[0])
    pop_ls2.append(item[1])
    act_ls2.append(item[2])
    pas_ls2.append(item[3])
    env1_ls2.append(item[4])
    env2_ls2.append(item[5])
plt.plot(idx_ls2, pop_ls2)
plt.plot(idx_ls2, act_ls2)
plt.plot(idx_ls2, pas_ls2)
plt.plot(idx_ls2, env1_ls2)
plt.plot(idx_ls2, env2_ls2)
plt.show()
