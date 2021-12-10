import random


class Organism():
    """
    This class defines the most basic version of an organism that can exist in
    our simulation.
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
    This class defines the most basic version of an environment that can exist
    in our simulation.
    """
    def __init__(self, food, refill_rate, population):
        """
        This method initializes an environment with certain instance
        attributes.
        """
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = population

    def update(self):
        """
        This method updates all organisms in an environment by passing the food
        as an argument and then uses these return values to change the
        environment attributes. Specifically it reduces the amount of food by
        the amount the organism ate, decides whether the organism should stay
        in the population, be deleted from it or be deleted from it while
        adding two daughter organisms. Daughter organisms have the same
        attributes as their parent but only half the size. In the end the food
        in the environment is refilled according to its instance attributes and
        the number of divisions that occured in this update is returned.
        """
        random.shuffle(self.population)

        no_of_divisions = 0
        new_organism_list = []

        for organism in self.population:
            divide, eaten_food = organism.update(self.food)
            # The food is decreased by the amount of food that organism ate.
            self.food = self.food - eaten_food
            # Dead organisms are skipped and therefore removed from the
            # population.
            if divide == "Dead":
                continue
            # If the organism returns the division signal True two daughter
            # organisms are created.
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

        # Then the food is increased by the refill_rate.
        self.food = self.food + self.refill_rate

        # The number of divisions per update is tracked and returned here.
        return no_of_divisions
