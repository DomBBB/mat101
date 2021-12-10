import random


class Organism():
    """
    This class extends the basic version of an organism and adds an excretion
    rate and implements that the organism excretes excrements when it is
    updated.
    """
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, excretion_rate, species="unknown"):
        """
        This method initializes an organism with certain instance attributes.
        """
        self.size = float(size)
        self.division_threshold = float(division_threshold)
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.excretion_rate = excretion_rate
        self.species = species
        self.alive = True

    def update(self, accumulated_excretions, len_population, available_food=None):
        """
        This method lets the organism eat food and burn already eaten food. It
        also tracks the excrements of this organism and then returns a state
        describing if the organism is dead or alive or if it wants to divide as
        well as the amount of food it ate and the amount of metabolites it
        excreted.
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
            # and decreases by a fraction of the accumulated excretions in the
            # environment and the amount of already eaten food that the
            # organism burns.
            self.size = self.size + uptake - accumulated_excretions/len_population/1000 - self.metabolic_rate(self.size)
            # This tracks the amount of excrements an organism excretes.
            excretion = self.excretion_rate(self.metabolic_rate(self.size))
            # Depending on the size of the organism different values are
            # returned to indicate its state, the amount of food it ate and the
            # amount of excrements it excreted.
            if self.size <= 0:
                self.alive = False
                return "Dead", float(uptake), float(excretion)
            if self.size > self.division_threshold:
                return True, float(uptake), float(excretion)
            else:
                return False, float(uptake), float(excretion)
        else:
            return "Dead", float(0), float(0)


class Environment():
    """
    This class extends the basic version of an environment and adds
    accumulating metabolite as well as the possibility to reduce it in the
    environment.
    """
    def __init__(self, food, refill_rate, population, reduce_metabolites):
        """
        This method initializes an environment with certain instance
        attributes.
        """
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = population
        self.accumulated_excretions = 0
        self.reduce_metabolites = reduce_metabolites

    def update(self):
        """
        This method updates all organisms in an environment by passing the food
        as an argument and then uses these return values to change the
        environment attributes. Specifically it reduces the amount of food by
        the amount the organism ate, decides whether the organism should stay
        in the population, be deleted from it or be deleted from it while
        adding two daughter organisms. In the end the food in the environment
        is refilled according to its instance attributes and the number of
        divisions that occured in this update is returned.
        """
        random.shuffle(self.population)

        no_of_divisions = 0
        new_organism_list = []

        for organism in self.population:
            # We introduce a new species called "excreter" that has different
            # behaviour than other organisms. If an organism is not of this
            # species it passes the normal parameters to its update function.
            if not organism.species == "excreter":
                divide, eaten_food, excreted = organism.update(self.accumulated_excretions, len(self.population), self.food)
                # Food is decreased by the amount of food that organism ate.
                self.food = self.food - eaten_food
                # Excrements are increased by the amount the organism excreted.
                self.accumulated_excretions = self.accumulated_excretions + excreted
            # If it is from this species the excrements accumulated in the
            # environment are passed as food to the organism's update function.
            # The other two parameters are chosen so that the accumulated
            # excrements do not harm the growth of the  excreters.
            else:
                divide, eaten_food, excreted = organism.update(0, 1, self.accumulated_excretions)
                # Excrements are decreased by the amount the excreter ate.
                self.accumulated_excretions = self.accumulated_excretions - eaten_food
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
                excretion_rate = organism.__dict__["excretion_rate"]
                species = organism.__dict__["species"]
                new_organism_list.append(Organism(size/2, division_threshold, uptake_rate, metabolic_rate, excretion_rate, species))
                new_organism_list.append(Organism(size/2, division_threshold, uptake_rate, metabolic_rate, excretion_rate, species))
                no_of_divisions = no_of_divisions + 1
            else:
                new_organism_list.append(organism)

        # After all organisms are updated the population is cleaned so that
        # only living organisms are contained in it.
        self.population = new_organism_list

        # Then the food is increased by the refill_rate.
        self.food = self.food + self.refill_rate

        # Also the excrements in the environment are reduced by a factor. This
        # can also be 1 for no reduction or more than 1 for an increase.
        self.accumulated_excretions = self.accumulated_excretions * self.reduce_metabolites

        # The number of divisions per update is tracked and returned here.
        return no_of_divisions
