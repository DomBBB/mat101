from Basic.basicOrganisms import Organism, Environment
import matplotlib.pyplot as plt

# CHANGE THESE (RATES) TO MAKE OTHER TESTS
organism_active = Organism(100, 200, lambda x : 5, lambda x : 2, "active")
organism_passive = Organism(100, 200, lambda x : 4, lambda x : 1, "passive")

# CHANGE THESE TO MAKE OTHER TESTS
environment = Environment(10**3, 1000, [organism_active, organism_passive])

res = []
for num in range(2*10**3):
    environment.update()
    active = 0
    passive = 0
    for organism in environment.population:
        if organism.species == "active":
            active += 1
        else:
            passive += 1
    res.append((num+1, len(environment.population), active, passive))
res
idx_ls = []
pop_ls = []
act_ls = []
pas_ls = []
for item in res:
    idx_ls.append(item[0])
    pop_ls.append(item[1])
    act_ls.append(item[2])
    pas_ls.append(item[3])
plt.plot(idx_ls, pop_ls)
plt.plot(idx_ls, act_ls)
plt.plot(idx_ls, pas_ls)
plt.show()
