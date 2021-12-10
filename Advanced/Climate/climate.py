import random


class Organism():
    """
    This class extends the basic version of an organism and introduces a new
    method and parameter to determine the current uptake and metabolic rate
    based on the temperature.
    """
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, species="unknown"):
        """
        This method initializes an organism with certain instance attributes.
        """
        self.size = float(size)
        self.division_threshold = float(division_threshold)
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.species = species
        self.alive = True

    def get_current_stats(self, temperature):
        """
        This method modifies the metabolic and uptake rates. At low temps rates
        set them to 0. At temps above zero there is a linear increase in uptake
        and metabolic rates.
        """
        if temperature < 0:
            current_metabolic_rate = 0
            current_uptake_rate = 0
        else:
            current_metabolic_rate = self.metabolic_rate(self.size) * (temperature/40)*2
            current_uptake_rate = self.uptake_rate(self.size) * (temperature/40)*2
        return current_metabolic_rate, current_uptake_rate

    def update(self, available_food=None, temperature=20):
        """
        This method lets the organism eat food and burn already eaten food
        according to the modified rate. It additionally lets an organism die
        if the temperature is to high. It then returns a state describing if the
        organism is dead or alive and if it wants to divide as well as the
        amount of food it ate.
        """
        if self.alive:
            current_metabolic_rate, current_uptake_rate = self.get_current_stats(temperature)
            # If update() is called without an argument this is considered as
            # an infinite amount of food and the organism eats as much as it
            # can take up.
            if available_food == None:
                uptake = current_uptake_rate
            # Otherwise it takes up whichever number from the passed food
            # amount and its own uptake is smaller.
            else:
                uptake = min(available_food, current_uptake_rate)
            # The size increases by the amount of food the organism can take up
            # and decreases by the amount of already eaten food that the
            # organism burns.
            self.size = self.size + uptake - current_metabolic_rate
            # Depending on the size of the organism and the temp, different
            # values are returned to indicate its state and the amount of food
            # it ate.
            if self.size <= 0:
                self.alive = False
                return "Dead", float(uptake)
            # This part captures the cell death probablity over 40 degrees,
            # the current temp gives a threshold and if random number is within
            # this threshold flag is changed
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
    """
    This class changes the basic version of an environment so that the
    temperature parameter influences the organisms and the environment.
    """
    def __init__(self, food, refill_rate, population, temperature_high, temperature_low):
        """
        This method initializes an environment with certain instance
        attributes.
        """
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = population
        self.temperature_high = float(temperature_high)
        self.temperature_low = float(temperature_low)
        self.temperature = 20
        self.temperature_medium = 20

    def season_cal(self, x1, y1, x2, y2, x3, y3, day):
    """
    This method constructs season parabolas and inputs the x value as the
    current day and returns the temperature.
    """
		    denom = (x1-x2) * (x1-x3) * (x2-x3);
		    A     = (x3 * (y2-y1) + x2 * (y1-y3) + x1 * (y3-y2)) / denom;
		    B     = (x3*x3 * (y1-y2) + x2*x2 * (y3-y1) + x1*x1 * (y2-y3)) / denom;
		    C     = (x2 * x3 * (x2-x3) * y1+x3 * x1 * (x3-x1) * y2+x1 * x2 * (x1-x2) * y3) / denom;
		    return A * (day ** 2)+ (B *day)+ C

    def modified_refill(self):
        """
        This method modifies the refill rate with low temps giving 0, below 30
        increasing to 1, below 40 decrease to 0, above 40 set to 0
        """
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
        """
        This method takes the current day, inputted temperatures and given the
        day constructed a inverted or regular parabola. The temperatures gives
        the three points to build the parabola and then the temperature is returned.
        """
        self.temperature_medium = (self.temperature_high+self.temperature_low)/2
        modded_day = current_day % 100

        if modded_day < 50:
        # Define your three known points
            x1,y1=[0,self.temperature_medium]
            x2,y2=[25,self.temperature_high]
            x3,y3=[50,self.temperature_medium]
        else:
        # Define your three known points
            x1,y1=[50,self.temperature_medium]
            x2,y2=[75,self.temperature_low]
            x3,y3=[100,self.temperature_medium]

        self.temperature = self.season_cal(x1, y1, x2, y2, x3, y3, modded_day)
        return self.temperature


    def update(self, num):
        """
        This method sets the temperature according to the season and then
        updates all organisms in an environment by passing the food and
        temperature as an argument and then uses these return values to change
        the environment attributes. Specifically it reduces the amount of food by
        the amount the organism ate, decides whether the organism should stay
        in the population, be deleted from it or stay and produce a daughter
        organism together with another organism. The daughter organism then
        takes its attributes randomly from one of both organisms and either
        keeps the species if both parents are the same or is from the type
        "mixed". In the end the food in the environment is refilled
        according to its instance attributes and the temperature and the number
        of divisions that occured in this update is returned.
        """
        # Sets the temperature according to the season.
        self.temperature = self.season_temperature(num)

        random.shuffle(self.population)

        no_of_divisions = 0
        new_organism_list = []

        for organism in self.population:
            divide, eaten_food = organism.update(self.food, self.temperature)
            # The food is decreased by the amount of food that organism ate.
            self.food = self.food - eaten_food
            # Dead organisms are skipped and therefore removed from the
            # population.
            if divide == "Dead":
                continue
            # If the organism returns the division signal True two daughter
            # organisms are created. They have the same attributes as the
            # parent organism but only half the size.
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

        # After all organisms are updated the population is cleaned so that
        # only living organisms are contained in it.
        self.population = new_organism_list

        # Then the refill rate is modified according to the temperature and the
        # food is increased by the refill_rate.
        current_refill_rate = self.modified_refill()
        self.food = self.food + current_refill_rate

        # The number of divisions per update is tracked and returned here.
        return no_of_divisions
