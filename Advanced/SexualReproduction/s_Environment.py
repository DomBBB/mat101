import random
from s_Organisms import Organism
class Environment():
    def __init__(self, food, refill_rate, population):
        self.food = float(food)
        self.refill_rate = float(refill_rate)
        self.population = list(population)

    def update(self):
        # Randomly shuffles a copy of the population list
            # AFTER shuffling we don't know the index in the original population:
            # --> WHY do we copy? Shouldn't we replace the population with the new population?
            # --> --> Do we remove dead ones?
        shuffle_list = self.population.copy()
        random.shuffle(shuffle_list)

        new_organism_list = []
        # Used to determine if there is an organism saved to pair with
        has_mate = False
        # For each organism in the shuffled list
        for organism in shuffle_list: 
            # Update the organism
            divide, eaten_food = organism.update(self.food)
            # Reduce food by the amount the organism ate.
            self.food = self.food - eaten_food

            # Not in task
                # If we want to remove dead organisms
            if divide == "Dead":
                continue
            # If the organism returns the division signal True: 
            # Save Organism Data and offer as Mate
            elif divide and not(has_mate):
                size = organism.__dict__["size"]
                fertility_threshold = organism.__dict__["fertility_threshold"]
                uptake_rate = organism.__dict__["uptake_rate"]
                metabolic_rate = organism.__dict__["metabolic_rate"]
                age_limit = organism.__dict__["age_limit"]
                has_mate = True
                new_organism_list.append(organism)
            elif divide and has_mate:
                size1 = organism.__dict__["size"]
                fertility_threshold1 = organism.__dict__["fertility_threshold"]
                uptake_rate1 = organism.__dict__["uptake_rate"]
                metabolic_rate1 = organism.__dict__["metabolic_rate"]
                age_limit1 = organism.__dict__["age_limit"]
                has_mate = False
                new_organism_list.append(organism)
                # Baby Organism
                new_organism_list.append(Organism(
                    size=random.choice([size, size1])/2, 
                    fertility_threshold=random.choice([fertility_threshold, fertility_threshold1]),
                    uptake_rate=random.choice([uptake_rate, uptake_rate1]),
                    metabolic_rate=random.choice([metabolic_rate, metabolic_rate1]),
                    age_limit=random.choice([age_limit1, age_limit]),
                    )) 
                
            else:
                new_organism_list.append(organism)

        self.population = new_organism_list
        # After all organisms have been updated, increase food by the refill_rate.
        self.food = self.food + self.refill_rate

        # Counts the total number of divisions that occur in an update cycle, and returns that value.
        return 
