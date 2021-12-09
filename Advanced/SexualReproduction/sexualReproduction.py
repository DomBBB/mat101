import random


class Organism():
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, age_limit, species="unknown"):
        self.size = float(size)
        self.division_threshold = float(division_threshold)
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.age_limit = age_limit
        self.species = species
        self.alive = True
        self.age = 0

    def update(self, available_food=None):
        if self.alive:
            self.age += 1
            if available_food == None:
                uptake = self.uptake_rate(self.size)
            else:
                uptake = min(available_food, self.uptake_rate(self.size))
            self.size = self.size + uptake - self.metabolic_rate(self.size)
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
    def __init__(self, food, refill_rate, population):
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = population

    def update(self):
        random.shuffle(self.population)

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        no_of_divisions = 0
        new_organism_list = []

        # Used to determine if there is an organism saved to pair with
        has_mate = False

        # For each organism in the shuffled list
        for organism in self.population:
            # Update the organism
            divide, eaten_food = organism.update(self.food)
            # Reduce food by the amount the organism ate.
            self.food = self.food - eaten_food
            # We remove dead organisms
            if divide == "Dead":
                continue
            # If the organism returns the division signal True: Check for mate, if no mate offer organism as next mate
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

        self.population = new_organism_list
        # After all organisms have been updated, increase food by the refill_rate.
        self.food = self.food + self.refill_rate

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        return no_of_divisions
