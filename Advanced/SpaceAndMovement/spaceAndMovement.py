import random
import math


class Organism:
    """
    This class extends the basic version of an organism and adds a position to
    the organism.
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
        self.organism_position = (random.randint(0,50), random.randint(0,50))
        self.alive = True

    def update(self, available_food=None):
        """
        This method lets the organism eat food and burn already eaten food. It
        then returns a state describing if the organism is dead or alive and if
        it wants to divide as well as the amount of food it ate.
        """
        if self.alive:
            # If update() is called without an argument this is considered as
            # an infinite amount of food and the organism eats as much as it
            # can take up.
            if available_food == None:
                uptake = self.uptake_rate(self.size)
            # Otherwise it takes up whichever number from the passed food
            # amount and its own uptake is smaller.
            else:
                uptake = min(available_food, self.uptake_rate(self.size))
            # The size increases by the amount of food the organism can take up
            # and decreases by the amount of already eaten food that the
            # organism burns.
            self.size = self.size + uptake - self.metabolic_rate(self.size)
            # Depending on the size of the organism different values are
            # returned to indicate its state and the amount of food it ate.
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
    """
    This class extends the basic version of an environment and adds randomly
    positioned food crates from which the organisms can eat when they are close
    enough.
    """
    def __init__(self, food, refill_rate, population, num_food_crates):
        """
        This method initializes an environment with certain instance
        attributes.
        """
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = population
        self.num_food_crates = num_food_crates
        self.food_crates = []
        for _ in range(0, num_food_crates):
            self.food_crates.append([random.randint(0, 50), random.randint(0, 50), food/num_food_crates])

    def update(self):
        """
        This method updates all organisms in an environment by calculating the
        distance to each food crate. If the organism is close enough food is
        passed as an argument and then those return values are used to change
        the environment attributes. Specifically it reduces the amount of food
        by the amount the organism ate, decides whether the organism should
        stay in the population, be deleted from it or be deleted from it while
        adding two daughter organisms. If the organism is not close enough it
        moves a random distance towards the crate. If a crate is emptied out it
        respawns at a random position. In the end the food crates in the
        environment are refilled according to the environment's attributes and
        the number of divisions that occured in this update is returned.
        """
        random.shuffle(self.population)

        no_of_divisions = 0
        new_organism_list = []

        for organism in self.population:
            # The first crate is set as closest crate and the distance from the
            # organism to this crate is calculated (pythagoras).
            closest_crate = self.food_crates[0]
            dist_to_closest = math.sqrt((closest_crate[0] - organism.organism_position[0])**2 + (closest_crate[1] - organism.organism_position[1])**2)

            # Then for each other crate the distance is also calculated
            # (pythagoras). If it is lower than the distance to the closest
            # this crate is temporarily set as closest.
            for crate in self.food_crates[1:]:
                x_crate = crate[0]
                y_crate = crate[1]
                dist = math.sqrt((x_crate - organism.organism_position[0])**2 + (y_crate - organism.organism_position[1])**2)
                if dist < dist_to_closest:
                    closest_crate = crate
                    dist_to_closest = dist

            # If the organism is close enough to the create the amount of food
            # in this crate is stored.
            if dist_to_closest <= 0.1:
                food_amount = closest_crate[2]
            # Otherwise the organism moves a random distance towards the
            # crate and 0 is stored as amount of food.
            else:
                directionx = closest_crate[0]-organism.organism_position[0]
                directiony = closest_crate[1]-organism.organism_position[1]
                food_amount = 0
                xval = organism.organism_position[0]
                xval = xval + random.randint(min(0, directionx), max(0, directionx))
                yval = organism.organism_position[1]
                yval = yval + random.randint(min(0, directiony), max(0, directiony))
                organism.organism_position = (xval, yval)

            # Update the organism
            divide, eaten_food = organism.update(food_amount)

            # Reduce food in food crate by the amount the organism ate.
            closest_crate[2] = closest_crate[2] - eaten_food
            # Respawn a crate at a random position if it is empty.
            if closest_crate[2] <= 0:
                self.food_crates.remove(closest_crate)
                self.food_crates.append([random.randint(0, 50),  random.randint(0, 50), 0])

            # Dead organisms are skipped and therefore removed from the
            # population.
            if divide == "Dead":
                continue
            # If the organism returns the division signal True two daughter
            # organisms are created. They have the same attributes as the
            # parent organism but only half the size and a random position.
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

        # Then the food in all crates is increased by an equal fraction of the
        # refill_rate.
        for crate in self.food_crates:
            crate[2] = crate[2] + self.refill_rate/self.num_food_crates

        # The number of divisions per update is tracked and returned here.
        return no_of_divisions
