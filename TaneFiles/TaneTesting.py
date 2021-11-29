import random
from typing import List
import matplotlib.pyplot as plt
from basicOrganisms import Organism
from basicEnvironment import Environment

# Tesiting Variable Sizes in Basic Organisms

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
environment1 = Environment(10**3, 100, [organism1])
for num in range(100):
    environment1.update()
len(environment1.population)

