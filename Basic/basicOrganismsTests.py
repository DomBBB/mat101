from Basic.basicOrganisms import Organism, Environment
import matplotlib.pyplot as plt

# CHANGE THESE SO LAWS THAT MAKE SENSE FOR A CERTAIN GEOMETRY --> disks, spheres, ...
organism1 = Organism(100, 200, lambda x : 1/4 * x**(2/3), lambda x : 1/50 * x, "Specimen One")
organism2 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Two")

for num in range(1000):
    organism1.update(4)
    organism2.update(4)
organism1.size
organism2.size


# CHANGE THESE TO MAKE OTHER TESTS
organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
environment1 = Environment(10**3, 100, [organism1])
for num in range(100):
    environment1.update()
len(environment1.population)

organism2 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
environment2 = Environment(10**3, 100, [organism2])
res2 = []
for num in range(5*10**3):
    environment2.update()
    res2.append((num+1, len(environment2.population)))
res2
idx_ls = []
pop_ls = []
for item in res2:
    idx_ls.append(item[0])
    pop_ls.append(item[1])
plt.plot(idx_ls, pop_ls)
plt.show()

organism3 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
environment3 = Environment(10**3, 100, [organism3])
res3 = []
for num in range(5*10**3):
    res3.append((num+1, environment3.update()))
res3
idx_ls = []
div_ls = []
for item in res3:
    idx_ls.append(item[0])
    div_ls.append(item[1])
plt.plot(idx_ls, div_ls)
plt.show()

organism4 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
environment4= Environment(10**3, 10**3, [organism4])
res4 = []
for num in range(5*10**3):
    environment4.update()
    res4.append((num+1, len(environment4.population)))
res4
idx_ls = []
pop_ls = []
for item in res4:
    idx_ls.append(item[0])
    pop_ls.append(item[1])
plt.plot(idx_ls, pop_ls)
plt.show()

organism5 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
environment5 = Environment(10**3, 10**3, [organism5])
res5 = []
for num in range(5*10**3):
    res5.append((num+1, environment5.update()))
res5
idx_ls = []
div_ls = []
for item in res5:
    idx_ls.append(item[0])
    div_ls.append(item[1])
plt.plot(idx_ls, div_ls)
plt.show()

#ENV(0, 100) oder (0, 1000)
organism6 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
environment6= Environment(0, 100, [organism6])
res6 = []
for num in range(5*10**3):
    environment6.update()
    res6.append((num+1, len(environment6.population)))
res6
idx_ls = []
pop_ls = []
for item in res6:
    idx_ls.append(item[0])
    pop_ls.append(item[1])
plt.plot(idx_ls, pop_ls)
plt.show()

#ENV(0, 100) oder (0, 1000)
organism7 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
environment7 = Environment(0, 100, [organism7])
res7 = []
for num in range(5*10**3):
    res7.append((num+1, environment7.update()))
res7
idx_ls = []
div_ls = []
for item in res7:
    idx_ls.append(item[0])
    div_ls.append(item[1])
plt.plot(idx_ls, div_ls)
plt.show()
