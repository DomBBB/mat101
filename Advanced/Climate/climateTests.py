from climate import Organism, Environment
import matplotlib.pyplot as plt
import pandas as pd

"""
CHANGE LAMBDA RATES TO OTHER VALUES TO OBTAIN DIFFERENT GRAPHS
"""
def save_climateTest1(file_folder):
    res = []
    labels = ["cycle", "season (num)"]

    for trial in range(3):
        organism_active = Organism(100, 200, lambda x : 5, lambda x : 2, "active")
        organism_passive = Organism(100, 200, lambda x : 5, lambda x : 2, "passive")
        environment1 = Environment(10**3, 10**3, [organism_active, organism_passive])
        labels.append("population_active" + "__t" + str(trial+1))
        labels.append("population_passive" + "__t" + str(trial+1))
        labels.append("population_total" + "__t" + str(trial+1))
        items = []
        items.append([0, 0, 1, 1, 2])

        for num in range(2*10**3):
            season = num
            while season > 100:
                season = season - 100
            environment1.update(num)
            active = 0
            passive = 0
            for organism in environment1.population:
                if organism.species == "active":
                    active += 1
                elif organism.species == "passive":
                    passive += 1
            assert((active+passive) == len(environment1.population))
            items.append([num+1, season+1, active, passive, active+passive])
        res.append(items)

    # STORE
    df = pd.DataFrame(columns=labels, index=range(len(res[0])))
    for idx, item in enumerate(res[0]):
        df.loc[idx] = pd.Series({labels[0]: res[0][idx][0],
                                               labels[1]: res[0][idx][1],
                                               labels[2]: res[0][idx][2],
                                               labels[3]: res[0][idx][3],
                                               labels[4]: res[0][idx][4],
                                               labels[5]: res[1][idx][2],
                                               labels[6]: res[1][idx][3],
                                               labels[7]: res[1][idx][4],
                                               labels[8]: res[2][idx][2],
                                               labels[9]: res[2][idx][3],
                                               labels[10]: res[2][idx][4]})

    df.to_csv(file_folder + "climateTest1.csv")

def retrieve_climateTest1(file_folder):
    df = pd.read_csv(file_folder + "climateTest1.csv", index_col=0)
    print(df)

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[2:5]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[5:8]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[8:11]:
        df[column].plot(ax=axes[2], x=df.columns[0], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

save_climateTest1("DataCollection/")
retrieve_climateTest1("DataCollection/")



organism_active = Organism(100, 200, lambda x : 5, lambda x : 2, "active")
organism_passive = Organism(100, 200, lambda x : 5, lambda x : 2, "passive")
environment1 = Environment(10**3, 10**3, [organism_active, organism_passive])

for num in range(100):
    environment1.update(num)
    print("-----------")
    for x in environment1.population:
        print("Population:", len(environment1.population))
        print("Season:", num)
        print("Size of each organism:", x.size)
