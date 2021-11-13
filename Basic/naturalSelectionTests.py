from mat101.basicOrganisms import Organism, Environment

# CHANGE THESE TO MAKE OTHER TESTS
organism_active = Organism(100, 200, lambda x : 5, lambda x : 2, "active")
organism_passive = Organism(100, 200, lambda x : 4, lambda x : 1, "passive")

environment = Environment(10**3, 100, [organism_active, organism_passive])

res = []

for num in range(2000):
    environment.update()
    act = 0
    pas = 0
    for x in environment.population:
        if x.species == "active":
            act += 1
        else:
            pas += 1
    res.append((len(environment.population), act, pas))

res
