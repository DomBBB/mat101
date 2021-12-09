from mutation import Organism, Environment
import matplotlib.pyplot as plt
import pandas as pd


"""
CHANGE LAMBDA RATES TO OTHER VALUES TO OBTAIN DIFFERENT GRAPHS
"""
def save_mutationTest1(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism_active = Organism(100, 200, lambda x : 5, lambda x : 2, "active")
        organism_passive = Organism(100, 200, lambda x : 4, lambda x : 1, "passive")
        environment1 = Environment(10**3, 10**3, [organism_active, organism_passive])
        labels.append("population_active" + "__t" + str(trial+1))
        labels.append("population_passive" + "__t" + str(trial+1))
        labels.append("population_total" + "__t" + str(trial+1))
        labels.append("mut_population_active" + "__t" + str(trial+1))
        labels.append("mut_population_passive" + "__t" + str(trial+1))
        labels.append("mut_population_total" + "__t" + str(trial+1))
        items = []
        items.append([0, 1, 1, 2, 0, 0, 0])

        for num in range(2*10**3):
            environment1.update()
            active = 0
            passive = 0
            mut_active = 0
            mut_passive = 0
            for organism in environment1.population:
                if organism.species.startswith("active"):
                    active += 1
                    if not organism.species == "active":
                        mut_active += 1
                elif organism.species.startswith("passive"):
                    passive += 1
                    if not organism.species == "passive":
                        mut_passive += 1
            assert((active+passive) == len(environment1.population))
            assert((mut_active+mut_passive) <= len(environment1.population))
            items.append([num+1, active, passive, active+passive, mut_active, mut_passive, mut_active + mut_passive])
        res.append(items)

    # STORE
    df = pd.DataFrame(columns=labels, index=range(len(res[0])))
    for idx, item in enumerate(res[0]):
        df.loc[idx] = pd.Series({labels[0]: res[0][idx][0],
                                               labels[1]: res[0][idx][1],
                                               labels[2]: res[0][idx][2],
                                               labels[3]: res[0][idx][3],
                                               labels[4]: res[0][idx][4],
                                               labels[5]: res[0][idx][5],
                                               labels[6]: res[0][idx][6],
                                               labels[7]: res[1][idx][1],
                                               labels[8]: res[1][idx][2],
                                               labels[9]: res[1][idx][3],
                                               labels[10]: res[1][idx][4],
                                               labels[11]: res[1][idx][5],
                                               labels[12]: res[1][idx][6],
                                               labels[13]: res[2][idx][1],
                                               labels[14]: res[2][idx][2],
                                               labels[15]: res[2][idx][3],
                                               labels[16]: res[2][idx][4],
                                               labels[17]: res[2][idx][5],
                                               labels[18]: res[2][idx][6]})

    df.to_csv(file_folder + "mutationTest1.csv")

def retrieve_mutationTest1(file_folder):
    df = pd.read_csv(file_folder + "mutationTest1.csv", index_col=0)
    print(df)

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:7]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[7:13]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[13:19]:
        df[column].plot(ax=axes[2], x=df.columns[0], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

# save_mutationTest1("DataCollection/")
retrieve_mutationTest1("DataCollection/")
