import random
from Mutation_Environment import MEnvironment
from Organism import Organism




organism1 = Organism(100, 200, lambda x : 1/4 * x**(2/3), lambda x : 1/50 * x, "SizeGuys")
organism2 = Organism(100, 200, lambda x : 5, lambda x : 2, "SpecimentZero")

environment1 = MEnvironment(10**3, 100, [organism1], [])


cap = 100

for round in range(0, cap):
    print(f"Round {round + 1}: ", end="")
    environment1.update()
