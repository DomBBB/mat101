from mat101.basicOrganisms import Organism, Environment

###
# Test Class Organism
###
# CHANGE THESE SO LAWS THAT MAKE SENSE FOR A CERTAIN GEOMETRY
organism1 = Organism(100, 200, lambda x : 1/4 * x**(2/3), lambda x : 1/50 * x, "Specimen Zero")
organism2 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")

organism2.update()
organism2.size

for num in range(100):
    organism2.update(0)
organism2.size

for num in range(1000):
    organism1.update(4)
    organism2.update(4)
organism1.size
organism2.size


###
# Test Class Environment
###
# CHANGE THESE TO MAKE OTHER TESTS
organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
environment1 = Environment(10**3, 100, [organism1])
for num in range(100):
    environment1.update()
len(environment1.population)

organism2 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
environment2 = Environment(10**3, 100, [organism2])
res2 = []
for num in range(5000):
    environment2.update()
    res2.append((num, len(environment2.population)))
res2

organism3 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
environment3 = Environment(10**3, 100, [organism3])
res3 = []
for num in range(5000):
    res3.append((num, environment3.update()))
res3

organism4 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
environment4= Environment(10**3, 10**3, [organism4])
res4 = []
for num in range(5000):
    environment4.update()
    res4.append((num, len(environment4.population)))
res4

organism5 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
environment5 = Environment(10**3, 10**3, [organism5])
res5 = []
for num in range(5000):
    res5.append((num, environment5.update()))
res5

organism6 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
environment6= Environment(0, 10**3, [organism6])
res6 = []
for num in range(5000):
    environment6.update()
    res6.append((num, len(environment6.population)))
res6

organism7 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
environment7 = Environment(0, 10**3, [organism7])
res7 = []
for num in range(5000):
    res7.append((num, environment7.update()))
res7
