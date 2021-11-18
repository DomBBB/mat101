import matplotlib.pyplot as plt

# Organism Class
class Organism():
    def __init__(self, size, fertility_threshold, uptake_rate, metabolic_rate, species = "unknown"):
        self.size = size
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.species = species
        self.alive = True
        self.fertility_threshold = fertility_threshold

    def update(self, available_food = None):
        if self.alive:
            print(available_food)
            if available_food == None:
                uptake = self.uptake_rate(self.size)
            else:
                uptake = min(available_food, self.uptake_rate(self.size))
            print(uptake)
            self.size = self.size + uptake - self.metabolic_rate(self.size)
            if self.size <= 0:
                self.alive = False
                return "Dead", float(uptake)
            if self.size > self.fertility_threshold:
                return True, float(uptake)
            else:
                return False, float(uptake)
        else:
            return "Dead", 0
