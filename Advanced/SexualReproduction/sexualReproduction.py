import random


class Organism():
    """
    This class extends the basic version of an organism and introduces an age
    and an age limit after which an organism dies.
    """
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, age_limit, species="unknown"):
        """
        This method initializes an organism with certain instance attributes.
        """
        self.size = float(size)
        self.division_threshold = float(division_threshold)
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.age_limit = age_limit
        self.species = species
        self.alive = True
        self.age = 0

    def update(self, available_food=None):
        """
        This method lets the organism eat food and burn already eaten food. It
        additionally makes the organism one year older and checks whether it
        reached the age limit and should die. It then returns a state describing
        if the organism is dead or alive and if it wants to divide as well as the
        amount of food it ate.
        """
        if self.alive:
            # The organism becomes one year older.
            self.age += 1
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
            # Depending on the size of the organism and its age, different
            # values are returned to indicate its state and the amount of food
            # it ate.
            if self.size <= 0 or self.age >= self.age_limit:
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
    This class changes the basic version of an environment so that two
    organisms need to mate together to produce an offspring.
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
        in the population, be deleted from it or stay and produce a daughter
        organism together with another organism. The daughter organism then
        takes its attributes randomly from one of both organisms and either
        keeps the species if both parents are the same or is from the type
        "mixed". In the end the food in the environment is refilled
        according to its instance attributes and the number of divisions that
        occured in this update as well as the number of mutations is returned.
        """
        random.shuffle(self.population)

        no_of_divisions = 0
        new_organism_list = []

        # Used to determine if there is an organism saved to pair with.
        has_mate = False

        for organism in self.population:
            divide, eaten_food = organism.update(self.food)
            # The food is decreased by the amount of food that organism ate.
            self.food = self.food - eaten_food
            # Dead organisms are skipped and therefore removed from the
            # population.
            if divide == "Dead":
                continue
            # If the organism returns the division signal True it checks
            # whether there already is a mate, otherwise it offers itself. If
            # there is a mate a daughter organism is created that randomly
            # takes the instance attributes from both parents and also defines
            # its species.
            elif divide and not(has_mate):
                size = organism.__dict__["size"]
                division_threshold = organism.__dict__["division_threshold"]
                uptake_rate = organism.__dict__["uptake_rate"]
                metabolic_rate = organism.__dict__["metabolic_rate"]
                age_limit = organism.__dict__["age_limit"]
                species = organism.__dict__["species"]
                has_mate = True
                new_organism_list.append(organism)
            elif divide and has_mate:
                size1 = organism.__dict__["size"]
                division_threshold1 = organism.__dict__["division_threshold"]
                uptake_rate1 = organism.__dict__["uptake_rate"]
                metabolic_rate1 = organism.__dict__["metabolic_rate"]
                age_limit1 = organism.__dict__["age_limit"]
                species1 = organism.__dict__["species"]
                has_mate = False
                new_organism_list.append(organism)
                if species == species1:
                    new_species = species1
                else:
                    new_species = "mixed"
                new_organism_list.append(Organism(
                    size=random.choice([size, size1])/2,
                    division_threshold=random.choice([division_threshold, division_threshold1]),
                    uptake_rate=random.choice([uptake_rate, uptake_rate1]),
                    metabolic_rate=random.choice([metabolic_rate, metabolic_rate1]),
                    age_limit=random.choice([age_limit1, age_limit]),
                    species=new_species))
                no_of_divisions = no_of_divisions + 1
            else:
                new_organism_list.append(organism)

        # After all organisms are updated the population is cleaned so that
        # only living organisms are contained in it.
        self.population = new_organism_list

        # Then the food is increased by the refill_rate.
        self.food = self.food + self.refill_rate

        # The number of divisions and mutations per update is tracked and
        # returned here.
        return no_of_divisions
