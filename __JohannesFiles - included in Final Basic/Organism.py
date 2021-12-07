import random


class Organism:
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, species="unknown"):
        self.size = float(size)
        self.division_threshold = float(division_threshold)
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.alive = True
        self.species = species

    def update(self, available_food=None):
        if available_food == None:
            uptake = self.uptake_rate(self.size)
        else:
            uptake = min(available_food, self.uptake_rate(self.size))
        if self.alive:
            self.size += uptake - self.metabolic_rate(self.size)
            if self.size <= 0:
                self.alive = False
                return False, float(uptake)
            if self.size >= self.division_threshold:
                return True, float(uptake)
            else:
                return False, float(uptake)
        else:
            return False, uptake
