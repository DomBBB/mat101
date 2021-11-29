import matplotlib.pyplot as plt
import random

# Organism Class
class Organism():
    def __init__(self, size, fertility_threshold, uptake_rate, metabolic_rate, species = "unknown"):
        self.size = size
        self.fertility_threshold = fertility_threshold
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.species = species
        self.alive = True
        self.age_limit = random.randint(80,100)
        self.age = 0
        

    def update(self, available_food = None):
        self.age += 1
        if self.alive:
            if available_food == None:
                uptake = self.uptake_rate(self.size)
            else:
                uptake = min(available_food, self.uptake_rate(self.size))
            self.size = self.size + uptake - self.metabolic_rate(self.size)
            if self.size <= 0 or self.age == self.age_limit:
                self.alive = False
                return "Dead", float(uptake)
            if self.size > self.fertility_threshold:
                return True, float(uptake)
            else:
                return False, float(uptake)
        else:
            return "Dead", 0

