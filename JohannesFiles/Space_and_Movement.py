import random
import math


class Organism:
    def __init__(self, size, division_threshold, uptake_rate, metabolic_rate, OrgPos, species="unknown"):
        self.size = float(size)
        self.division_threshold = float(division_threshold)
        self.uptake_rate = uptake_rate
        self.metabolic_rate = metabolic_rate
        self.alive = True
        self.species = species

        x = random.randint(0, 50)
        y = random.randint(0, 50)
        self.OrgPos = (x, y)



    def update(self, available_food=None):


        if available_food == None:
            uptake = self.uptake_rate(self.size)
        else:
            uptake = min(available_food, self.uptake_rate(self.size))


        if self.alive:
            self.size -= self.metabolic_rate(self.size)
            if self.size <= 0:
                self.alive = False
                return False, float(uptake)
            if self.size >= self.division_threshold:
                return True, float(uptake)
            else:
                return False, float(uptake)
        else:
            return False, uptake


class Environment():
    def __init__(self, food, refill_rate, food_crate, population,):
        self.food = food
        self.refill_rate = float(refill_rate)
        self.population = population
        self.DivNum = 0
        self.food_devider = food_crate
        self.food_crate = []
        for _ in range(0, food_crate):
            x = random.randint(0, 50)
            y = random.randint(0, 50)
            self.food_crate.append([x, y, food/food_crate])


    def update(self):

        shuffle_list = self.population.copy()
        random.shuffle(shuffle_list)


        for organism in shuffle_list:


            salami = 0

            closest_crate = self.food_crate[0]

            for crate in self.food_crate:
                x_crate = crate[0]
                y_crate = crate[1]
                z_crate = crate[2]

                distance = lambda x,y: math.sqrt(abs(x - organism.OrgPos[0])**2+abs(y - organism.OrgPos[1])**2)

                dist = distance(x_crate, y_crate)
                dist1 = distance(closest_crate[0], closest_crate[1])

                if dist < dist1:
                    closest_crate = crate

                    salami = dist
            self.food_crate.remove(closest_crate)

            directionx = closest_crate[0]-organism.OrgPos[0]
            directiony = closest_crate[1]-organism.OrgPos[1]



            food_amount = 0

            if salami <= 0.1:

                food_amount = closest_crate[2]

            else:
                uptake = 0

                xval = organism.OrgPos[0]
                xval += random.randint(min(0, directionx), max(0, directionx))

                yval = organism.OrgPos[1]
                yval += random.randint(min(0, directiony), max(0, directiony))

                organism.OrgPos = (xval, yval)

            ready_to_divide, uptake = organism.update(food_amount)

            closest_crate[2] -= uptake
            self.food_crate.append(closest_crate)



            organism.size += uptake

            if ready_to_divide:

                newOrganism = lambda organism: Organism(organism.size/2, organism.division_threshold, organism.uptake_rate, organism.metabolic_rate, organism.OrgPos,  organism.species)
                org1 = newOrganism(organism)
                org2 = newOrganism(organism)
                self.population.append(org1)
                self.population.append(org2)
                self.population.remove(organism)
                self.DivNum += 1


        for crate in self.food_crate:
            crate[2] += self.refill_rate/self.food_devider

        print(f"units, no. divisions: {self.DivNum}, population: {len(self.population)}, CratePos: {self.food_crate}, Organism Pos: {organism.OrgPos}, Organsim Size {organism.size} ")




organism1 = Organism(100, 200, lambda x : 1/4 * x**(2/3), lambda x : 1/50 * x, "SizeGuys")
organism2 = Organism(100, 200, lambda x : 5, lambda x : 2, "SpecimentZero")

environment1 = Environment(10**3, 10, 5, [organism1, organism2])


cap = 100

for round in range(0, cap):
    print(f"Round {round + 1}: ", end="")
    environment1.update()

print(environment1.food_crate)
print(organism1.size)
