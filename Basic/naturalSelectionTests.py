from basicOrganismsAndEnvironment import Organism, Environment
import matplotlib.pyplot as plt
import pandas as pd


def naturalSelectionTest(file_folder=None):
    res = []
    labels = []

    for trial in range(3):
        organism_active = Organism(100, 200, lambda x : 5, lambda x : 2, "active")
        organism_passive = Organism(100, 200, lambda x : 4, lambda x : 1, "passive")
        environment1 = Environment(10**3, 10**3, [organism_active, organism_passive])
        labels.append("cycle" + "__t" + str(trial+1))
        labels.append("population_active" + "__t" + str(trial+1))
        labels.append("population_passive" + "__t" + str(trial+1))
        labels.append("population_total" + "__t" + str(trial+1))
        items = []
        items.append([0, 1, 1, 2])

        for num in range(2*10**3):
            environment1.update()
            active = 0
            passive = 0
            for organism in environment1.population:
                if organism.species == "active":
                    active += 1
                elif organism.species == "passive":
                    passive += 1
            assert((active+passive) == len(environment1.population))
            items.append([num+1, active, passive, active+passive])
        res.append(items)

    # STORE
    df = pd.DataFrame(columns=labels, index=range(len(res[0])))
    for idx, item in enumerate(res[0]):
        df.loc[idx] = pd.Series({labels[0]: res[0][idx][0],
                                               labels[1]: res[0][idx][1],
                                               labels[2]: res[0][idx][2],
                                               labels[3]: res[0][idx][3],
                                               labels[4]: res[1][idx][0],
                                               labels[5]: res[1][idx][1],
                                               labels[6]: res[1][idx][2],
                                               labels[7]: res[1][idx][3],
                                               labels[8]: res[2][idx][0],
                                               labels[9]: res[2][idx][1],
                                               labels[10]: res[2][idx][2],
                                               labels[11]: res[2][idx][3]})

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:4]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[5:8]:
        df[column].plot(ax=axes[1], x=df.columns[4])
    for column in df.columns[9:12]:
        df[column].plot(ax=axes[2], x=df.columns[8], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

    df
    #df.to_csv(file_folder + "naturalSelectionTest.csv")
    # df = pd.read_csv(file_folder + "naturalSelectionTest.csv", index_col=0)
