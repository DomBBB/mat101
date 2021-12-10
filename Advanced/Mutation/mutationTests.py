from mutation import Organism, Environment
import matplotlib.pyplot as plt
import pandas as pd


def save_mutationTest1(file_folder):
    """
    This function stores the results from this test that is done in triplicate
    in a csv file.
    """
    res = []
    labels = ["cycle"]

    # The simulation is done three times to account for randomness in the
    # results. Corresponding labels are created and the results are
    # appended to a list.
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

    # An empty dataframe with the labels and an appropriate number of entries
    # is created and then filled with the corresponding values.
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

    # The dataframe is stored as a csv file.
    df.to_csv(file_folder + "mutationTest1.csv")

def retrieve_mutationTest1(file_folder):
    """
    This function retrieves the results from this test from a csv file and
    plots all trials.
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "mutationTest1.csv", index_col=0)

    # An empty plot with subplots is created and formating attributes are
    # defined.
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    # The subplots are filled with the corresponding data.
    for column in df.columns[[1, 2, 4, 5]]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[[7, 8, 10, 11]]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[[13, 14, 16, 17]]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    # The plot is labeled properly.
    axes[0].set_title("Mutation", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Active: 5 & 2", "Passive: 4 & 1", "Mutated Active", "Mutated Passive"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_mutationTest1__t1(file_folder):
    """
    This function retrieves the results from this test from a csv file and
    plots only one trial.
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "mutationTest1.csv", index_col=0)

    # An empty plot with one subplot is created and formatting attributes are
    # defined.
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    # The subplot is filled with the corresponding data.
    for column in df.columns[[1, 2, 4, 5]]:
        df[column].plot(ax=axes, x=df.columns[0])

    # The plot is labeled properly.
    axes.set_title("Mutation - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Active: 5 & 2", "Passive: 4 & 1", "Mutated Active", "Mutated Passive"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_mutationTest1("DataCollection/")
retrieve_mutationTest1("DataCollection/")
retrieve_mutationTest1__t1("DataCollection/")


def save_mutationTest2(file_folder):
    """
    This function stores the results from this test that is done in triplicate
    in a csv file.
    """
    res = []
    labels = ["cycle"]

    # The simulation is done three times to account for randomness in the
    # results. Corresponding labels are created and the results are
    # appended to a list.
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
        for num in range(4*10**3):
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

    # An empty dataframe with the labels and an appropriate number of entries
    # is created and then filled with the corresponding values.
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

    # The dataframe is stored as a csv file.
    df.to_csv(file_folder + "mutationTest2.csv")

def retrieve_mutationTest2(file_folder):
    """
    This function retrieves the results from this test from a csv file and
    plots all trials.
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "mutationTest2.csv", index_col=0)

    # An empty plot with subplots is created and formating attributes are
    # defined.
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    # The subplots are filled with the corresponding data.
    for column in df.columns[[1, 2, 4, 5]]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[[7, 8, 10, 11]]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[[13, 14, 16, 17]]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    # The plot is labeled properly.
    axes[0].set_title("Mutation", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Active: 5 & 2", "Passive: 4 & 1", "Mutated Active", "Mutated Passive"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_mutationTest2__t1(file_folder):
    """
    This function retrieves the results from this test from a csv file and
    plots only one trial.
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "mutationTest2.csv", index_col=0)

    # An empty plot with one subplot is created and formatting attributes are
    # defined.
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    # The subplot is filled with the corresponding data.
    for column in df.columns[[1, 2, 4, 5]]:
        df[column].plot(ax=axes, x=df.columns[0])

    # The plot is labeled properly.
    axes.set_title("Mutation - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Active: 5 & 2", "Passive: 4 & 1", "Mutated Active", "Mutated Passive"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_mutationTest2("DataCollection/")
retrieve_mutationTest2("DataCollection/")
retrieve_mutationTest2__t1("DataCollection/")
