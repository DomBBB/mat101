import random


class Organism():
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, species="unknown"):
        self.size = float(size)
        self.division_threshold = float(division_threshold)
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.species = species
        self.alive = True

    def get_current_stats(self, temperature):
        if temperature < 0:
            current_metabolic_rate = 0
            current_uptake_rate = 0
        else:
            current_metabolic_rate = self.metabolic_rate(self.size) * (temperature/40)*2
            current_uptake_rate = self.uptake_rate(self.size) * (temperature/40)*2
        return current_metabolic_rate, current_uptake_rate

    def update(self, available_food=None, temperature=20):
        if self.alive:
            current_metabolic_rate, current_uptake_rate = self.get_current_stats(temperature)
            if available_food == None:
                uptake = current_uptake_rate
            else:
                uptake = min(available_food, current_uptake_rate)
            self.size = self.size + uptake - current_metabolic_rate
            if self.size <= 0:
                self.alive = False
                return "Dead", float(uptake)
            # add a part here if the temp is above a certain temp then death
            if temperature > 40:
                temp_threshold = ((temperature-40)/10)**2
                organisms_life_number = random.uniform(0, 1)
                if organisms_life_number < temp_threshold:
                    self.alive = False
                    return "Dead", float(uptake)
            if self.size > self.division_threshold:
                return True, float(uptake)
            else:
                return False, float(uptake)
        else:
            return "Dead", float(0)


class Environment():
    def __init__(self, food, refill_rate, population, temperature_high, temperature_low):
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = population
        self.temperature_high = float(temperature_high)
        self.temperature_low = float(temperature_low)
        self.temperature = 20
        self.temperature_medium = 20

    def season_cal(self, x1, y1, x2, y2, x3, y3, day):
		    denom = (x1-x2) * (x1-x3) * (x2-x3);
		    A     = (x3 * (y2-y1) + x2 * (y1-y3) + x1 * (y3-y2)) / denom;
		    B     = (x3*x3 * (y1-y2) + x2*x2 * (y3-y1) + x1*x1 * (y2-y3)) / denom;
		    C     = (x2 * x3 * (x2-x3) * y1+x3 * x1 * (x3-x1) * y2+x1 * x2 * (x1-x2) * y3) / denom;
		    return A * (day ** 2)+ (B *day)+ C

    def modified_refill(self):
        if self.temperature < 0:
          current_refill_rate = 0
        elif self.temperature <= 30:
            current_refill_rate = (self.temperature/30)*self.refill_rate
        elif self.temperature <= 40:
            current_refill_rate = ((-0.1*self.temperature)+4)*self.refill_rate
        else:
          current_refill_rate = 0
        return current_refill_rate

    def season_temperature(self, current_day):
        self.temperature_medium = (self.temperature_high+self.temperature_low)/2
        modded_day = current_day % 100

        if modded_day < 50:
        #Define your three known points
            x1,y1=[0,self.temperature_medium]
            x2,y2=[25,self.temperature_high]
            x3,y3=[50,self.temperature_medium]

        else:
        #Define your three known points
            x1,y1=[50,self.temperature_medium]
            x2,y2=[75,self.temperature_low]
            x3,y3=[100,self.temperature_medium]

        self.temperature = self.season_cal(x1, y1, x2, y2, x3, y3, modded_day)
        return self.temperature


    def update(self, num):
        self.temperature = self.season_temperature(num)

        random.shuffle(self.population)

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
