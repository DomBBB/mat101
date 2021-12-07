from Final.Basic.basicOrganismsAndEnvironment import Organism, Environment
import matplotlib.pyplot as plt
import pandas as pd


# CHANGE THESE TO LAWS THAT MAKE SENSE FOR A CERTAIN GEOMETRY --> disks, spheres, ...

def save_basicTest_variableSize(file_folder=None):
    res = []
    labels = []

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 1/4 * x**(2/3), lambda x : 1/50 * x, "Specimen One")
        organism2 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Two")
        labels.append("cycle" + "__t" + str(trial+1))
        labels.append("organismsize_variableRate" + "__t" + str(trial+1))
        labels.append("organismsize_fixedRate" + "__t" + str(trial+1))
        items = []
        for num in range(1001):
            items.append([num, organism1.size, organism2.size])
            organism1.update()
            organism2.update()
        res.append(items)

    # STORE
    df = pd.DataFrame(columns=labels, index=range(len(res[0])))
    for idx, item in enumerate(res[0]):
        df.loc[idx] = pd.Series({labels[0]: res[0][idx][0],
                                               labels[1]: res[0][idx][1],
                                               labels[2]: res[0][idx][2],
                                               labels[3]: res[1][idx][0],
                                               labels[4]: res[1][idx][1],
                                               labels[5]: res[1][idx][2],
                                               labels[6]: res[2][idx][0],
                                               labels[7]: res[2][idx][1],
                                               labels[8]: res[2][idx][2]})


    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:3]:
        df[column].plot(ax=axes[0], x=df.columns[0], label=column)
    for column in df.columns[4:6]:
        df[column].plot(ax=axes[1], x=df.columns[3], label=column)
    for column in df.columns[7:9]:
        df[column].plot(ax=axes[2], x=df.columns[6], label=column)

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

    df
    # df.to_csv(file_folder + "_basicTest_variableSize")
    # df = pd.read_csv(file_folder + "_basicTest_variableSize", index_col=0)

# CHANGE THESE TO TEST DIFFERENT THINGS

def save_basicTest_Environment1(file_folder=None):
    res = []
    labels = []

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Zero")
        environment1 = Environment(10**3, 100, [organism1])
        labels.append("cycle" + "__t" + str(trial+1))
        labels.append("population" + "__t" + str(trial+1))
        items = []
        for num in range(1001):
            items.append([num, len(environment1.population)])
            environment1.update()
        res.append(items)

    # STORE
    df = pd.DataFrame(columns=labels, index=range(len(res[0])))
    for idx, item in enumerate(res[0]):
        df.loc[idx] = pd.Series({labels[0]: res[0][idx][0],
                                               labels[1]: res[0][idx][1],
                                               labels[2]: res[1][idx][0],
                                               labels[3]: res[1][idx][1],
                                               labels[4]: res[2][idx][0],
                                               labels[5]: res[2][idx][1]})

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0], label=column)
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[1], x=df.columns[2], label=column)
    for column in df.columns[5:6]:
        df[column].plot(ax=axes[2], x=df.columns[4], label=column)

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

    df
    #df.to_csv(file_folder + "_basicTest_variableSize")







organism1 = Organism(100, 200, lambda x : 1/4 * x**(2/3), lambda x : 1/50 * x, "SizeGuys")
organism2 = Organism(100, 200, lambda x : 5, lambda x : 2, "SpecimentZero")

environment1 = Environment(10**3, 100, [organism1])


cap = 100

for round in range(0, cap):
    print(f"Round {round + 1}: ", end="")
    environment1.update()





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
