import random
from typing import List
import matplotlib.pyplot as plt
from s_Organisms import Organism
from s_Environment import Environment
import pandas as pd

# Two Organisms with same paramers/ Variable Refill Rate
organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, 10000)
organism2 = Organism(100, 200, lambda x : 5, lambda x : 2, 10000)
environment1 = Environment(1000, 10, [organism1, organism2])
environment2 = Environment(1000, 100, [organism1, organism2])
environment3 = Environment(1000, 500, [organism1, organism2])

time =[0]
pop_size1 = [len(environment1.population)]
pop_size2 = [len(environment2.population)]
pop_size3 = [len(environment3.population)]
for num in range(10000):
    environment1.update()
    environment2.update()
    environment3.update()
    time.append(num + 1)
    pop_size1.append(len(environment1.population))
    pop_size2.append(len(environment2.population))
    pop_size3.append(len(environment3.population))

# Font for Plot

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

# Plot       

plt.plot(time, pop_size1, label = "10")
plt.plot(time, pop_size2, label = "100")
plt.plot(time, pop_size3, label = "500")
plt.title("Varying Refill Rate", fontdict=font)
plt.ylabel("Population Size")
plt.xlabel("Time")
plt.legend()
plt.show()


# Food is fixed and age is variable
organism1_100 = Organism(100, 200, lambda x : 5, lambda x : 2, 100)
organism2_100 = Organism(100, 200, lambda x : 5, lambda x : 2, 100)

organism1_300 = Organism(100, 200, lambda x : 5, lambda x : 2, 300)
organism2_300 = Organism(100, 200, lambda x : 5, lambda x : 2, 300)

organism1_500 = Organism(100, 200, lambda x : 5, lambda x : 2, 500)
organism2_500 = Organism(100, 200, lambda x : 5, lambda x : 2, 500)



environment1 = Environment(1000, 500, [organism1_100, organism2_100])
environment2 = Environment(1000, 500, [organism1_300, organism2_300])
environment3 = Environment(1000, 500, [organism1_500, organism2_500])

time =[0]
pop_size1 = [len(environment1.population)]
pop_size2 = [len(environment2.population)]
pop_size3 = [len(environment3.population)]

for num in range(10000):
    environment1.update()
    environment2.update()
    environment3.update()
    time.append(num + 1)
    pop_size1.append(len(environment1.population))
    pop_size2.append(len(environment2.population))
    pop_size3.append(len(environment3.population))

plt.plot(time, pop_size1, label = "Population_100")
plt.plot(time, pop_size2, label = "Population_300")
plt.plot(time, pop_size3, label = "Population_500")
plt.title("Varying Age Limit", fontdict=font)
plt.ylabel("Population Size")
plt.xlabel("Time")
plt.legend()
plt.show()
    


# Ploting the Amount of Food vs. Population Size

organism1 = Organism(100 , 200, lambda x: 5, lambda x: 2, 300)
organism2 = Organism(100 , 200, lambda x: 5, lambda x: 2, 300)

environment1 = Environment(1000, 500, [organism1, organism2])

available_food = [environment1.food]
time = [0]
pop_size1 = [len(environment1.population)]

for num in range(2000):
    environment1.update()
    time.append(num + 1)
    pop_size1.append(len(environment1.population))
    available_food.append(environment1.food)

fig,ax=plt.subplots()
ax.plot(time, pop_size1, color = "red", marker=".")
ax.set_xlabel("Time", fontsize=14)
ax.set_ylabel("Population Size", color = "red", fontsize=14)
ax.set_title("Available Food vs. Population Size", fontsize = 20)
ax2=ax.twinx()
ax2.plot(time, available_food, color = "blue", marker=".")
ax2.set_ylabel("Availabe Food", color = "blue", fontsize=14)
plt.show()













