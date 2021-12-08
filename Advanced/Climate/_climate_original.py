#Original Code

import random

class Organism():
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, species="unknown"):
        self.size = float(size)
        self.division_threshold = float(division_threshold)
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.species = species
        self.alive = True

    def get_current_stats(self, temperature): #this code applies a temperature modifer, temperature increases linearly metabolic_rate and uptake peak at 40
        current_metabolic_rate = self.metabolic_rate(self.size) * (temperature/40)*2
        current_uptake_rate = self.uptake_rate(self.size) * (temperature/40)*2
        return current_metabolic_rate, current_uptake_rate

    def update(self, available_food=None, temperature = 20):
        current_metabolic_rate, current_uptake_rate = self.get_current_stats(temperature)
        if self.alive:
            if available_food == None:
                uptake = current_uptake_rate # self.uptake_rate(self.size)
            else:
                uptake = min(available_food, current_uptake_rate) #self.uptake_rate(self.size)) changes to be edited
            self.size = self.size + uptake - current_metabolic_rate # self.metabolic_rate(self.size) changes to be edited
            if self.size <= 0:
                self.alive = False
                return "Dead", float(uptake)
            if self.size > self.division_threshold:
                return True, float(uptake)
            else:
                return False, float(uptake)
        else:
            return "Dead", float(0)



class Environment():
    def __init__(self, food, refill_rate, population):
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = population
        self.temperature = 20

    def modified_refill(self): #this function applies a temperature modifer to refill_rate, linear increase from 0 to 30 peak of 1, then decrease from 40
        if self.temperature <= 30:
            current_refill_rate = (self.temperature/30)*self.refill_rate
        else:
            current_refill_rate = ((-0.1*self.temperature)+4)*self.refill_rate
        return current_refill_rate

#this function applies a seasonal temperature using updates as days, 0 to 25 days  spring linear increase from 0 to 30 temperature,
#25 to 50 days summer parabola from 30 temp peak at 40 then back to 30, 50 to 75 days linear decrease from 30 to 10 temperature,
#75 to 100 days winter parabola of temperature 10 to low of 0 then back to 10 temperature
    def season_temperature(self, current_day):
        modded_day = current_day % 100
        if modded_day < 25:
            temperature = (0.8 * modded_day) + 10
        elif modded_day < 50:
            temperature = -0.064 * (modded_day ** 2)+ (48 *modded_day)-50
        elif modded_day < 75:
            temperature = (-0.8 * modded_day) + 70
        else:
            temperature = 0.064 * (modded_day ** 2) - (11.2 * modded_day) + 490
        return temperature

    def update(self, num):#modidy update to take in number of updates
        random.shuffle(self.population)

        self.temperature = self.season_temperature(num)


        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        no_of_divisions = 0
        new_organism_list = []

        # For each organism in the shuffled list
        for organism in self.population:
            # Update the organism
            divide, eaten_food = organism.update(self.food, self.temperature)
            # Reduce food by the amount the organism ate.
            self.food = self.food - eaten_food
            # We remove dead organisms
            if divide == "Dead":
                continue
            # If the organism returns the division signal True: Remove organism from population & add 2 new (same parameters, size/2)
            elif divide:
                size = organism.__dict__["size"]
                division_threshold = organism.__dict__["division_threshold"]
                uptake_rate = organism.__dict__["uptake_rate"]
                metabolic_rate = organism.__dict__["metabolic_rate"]
                species = organism.__dict__["species"]
                new_organism_list.append(Organism(size/2, division_threshold, uptake_rate, metabolic_rate, species))
                new_organism_list.append(Organism(size/2, division_threshold, uptake_rate, metabolic_rate, species))
                no_of_divisions = no_of_divisions + 1
            else:
                new_organism_list.append(organism)

        self.population = new_organism_list
        # After all organisms have been updated, increase food by the refill_rate.
        current_refill_rate = self.modified_refill()
        self.food = self.food + current_refill_rate

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        return no_of_divisions
