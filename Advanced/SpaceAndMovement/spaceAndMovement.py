import random
import math


class Organism:
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, species="unknown"):
        self.size = float(size)
        self.division_threshold = float(division_threshold)
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.species = species
        self.organism_position = (random.randint(0,50), random.randint(0,50))
        self.alive = True

    def update(self, available_food=None):
        if self.alive:
            if available_food == None:
                uptake = self.uptake_rate(self.size)
            else:
                uptake = min(available_food, self.uptake_rate(self.size))
            self.size = self.size + uptake - self.metabolic_rate(self.size)
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
    def __init__(self, food, refill_rate, population, num_food_crates):
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = population
        self.num_food_crates = num_food_crates
        self.food_crates = []
        for _ in range(0, num_food_crates):
            self.food_crates.append([random.randint(0, 50), random.randint(0, 50), food/num_food_crates])

    def update(self):
        random.shuffle(self.population)

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        no_of_divisions = 0
        new_organism_list = []

        # For each organism in the shuffled list
        for organism in self.population:

            closest_crate = self.food_crates[0]
            dist_to_closest = math.sqrt((closest_crate[0] - organism.organism_position[0])**2 + (closest_crate[1] - organism.organism_position[1])**2)
            food_in_closest = closest_crate[2]

            for crate in self.food_crates:
                x_crate = crate[0]
                y_crate = crate[1]

                dist = math.sqrt((x_crate - organism.organism_position[0])**2 + (y_crate - organism.organism_position[1])**2)
                if dist < dist_to_closest:
                    closest_crate = crate
                    dist_to_closest = dist

            directionx = closest_crate[0]-organism.organism_position[0]
            directiony = closest_crate[1]-organism.organism_position[1]

            if dist_to_closest <= 0.1:
                food_amount = closest_crate[2]
            else:
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
            if closest_crate[2] <= 0:
                self.food_crates.remove(closest_crate)
                self.food_crates.append([random.randint(0, 50),  random.randint(0, 50), 0])
            else:
                closest_crate[2] = closest_crate[2] - eaten_food

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
        for crate in self.food_crates:
            crate[2] = crate[2] + self.refill_rate/self.num_food_crates

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        return no_of_divisions
