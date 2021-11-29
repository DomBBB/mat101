import random
from typing import List
import matplotlib.pyplot as plt
from basicOrganisms import Organism
from advancedEnvironment import Environment



"""  # Tesiting Variable Sizes in Basic Organisms

organism1 = Organism(100, 200, lambda x: 1/4*x**(2/3), lambda x: 1/50*x, "SizeGuys")
organism2 = Organism(100, 200, lambda x: 5, lambda x: 2, "Specimen Zero")
org1size = [organism1.size]
org2size = [organism2.size]
time = list(range(1001))
for i in range(10**3):
    organism1.update()
    organism2.update()
    org1size.append(organism1.size)
    org2size.append(organism2.size)


plt.plot(time, org1size, label = "variable Rate")
plt.plot(time, org2size, label = "fixed Rate")
plt.legend()
plt.show()

# Testing basicEnvironment

organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
environment1 = Environment(food = 1000, refill_rate =1000, population=[organism1])
population_size = []
for num in range(5*10**3):
    environment1.update()
    population_size.append(len(environment1.population))

time = range(5*10**3)

plt.plot(time, population_size, label = "Population")
plt.legend()
plt.show() """

# Testing makingBabys
organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "active")
organism2 = Organism(90, 180, lambda x : 4, lambda x : 1, "passive")
environment = Environment(1000, 1000, [organism1, organism2])
kids = 0
time = [0]
pop_size = [len(environment.population)]
for num in range(5000):
    kids += environment.update()
    time.append(num + 1)
    pop_size.append(len(environment.population))

print(kids)

plt.plot(time, pop_size)
plt.show()
