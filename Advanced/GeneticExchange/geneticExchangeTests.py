from geneticExchange import Organism, Environment
import matplotlib.pyplot as plt
import pandas as pd


def save_geneticExchangeTest1(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism_active = Organism(100, 200, lambda x : 5, lambda x : 2, "active")
        organism_passive = Organism(100, 200, lambda x : 4, lambda x : 1, "passive")
        active_uptake_original = organism_active.uptake_rate(1)
        active_metabolite_original = organism_active.uptake_rate(1)
        environment1 = Environment(10**3, 1000, [organism_active, organism_passive])
        labels.append("population_active" + "__t" + str(trial+1))
        labels.append("population_passive" + "__t" + str(trial+1))
        labels.append("population_total" + "__t" + str(trial+1))
        labels.append("uptake_active" + "__t" + str(trial+1))
        labels.append("uptake_passive" + "__t" + str(trial+1))
        labels.append("metabolic_active" + "__t" + str(trial+1))
        labels.append("metabolic_passive" + "__t" + str(trial+1))
        items = []
        items.append([0, 1, 1, 2, 1, 1, 1, 1])

        for num in range(2*10**3):
            environment1.update()
            active = 0
            passive = 0
            attributes = {"up_active": 0, "up_passive": 0, "me_active": 0, "me_passive": 0}
            for organism in environment1.population:
                if organism.species == "active":
                    active += 1
                elif organism.species == "passive":
                    passive += 1
                if organism.uptake_rate(1) == active_uptake_original:
                    attributes["up_active"] = attributes["up_active"] + 1
                else:
                    attributes["up_passive"] = attributes["up_passive"] + 1
                if organism.metabolic_rate(1) == active_metabolite_original:
                    attributes["me_active"] = attributes["me_active"] + 1
                else:
                    attributes["me_passive"] = attributes["me_passive"] + 1
            assert((active+passive) == len(environment1.population))
            items.append([num+1, active, passive, active+passive, attributes["up_active"], attributes["up_passive"], attributes["me_active"], attributes["me_passive"]])
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
                                               labels[7]: res[0][idx][7],
                                               labels[8]: res[1][idx][1],
                                               labels[9]: res[1][idx][2],
                                               labels[10]: res[1][idx][3],
                                               labels[11]: res[1][idx][4],
                                               labels[12]: res[1][idx][5],
                                               labels[13]: res[1][idx][6],
                                               labels[14]: res[1][idx][7],
                                               labels[15]: res[2][idx][1],
                                               labels[16]: res[2][idx][2],
                                               labels[17]: res[2][idx][3],
                                               labels[18]: res[2][idx][4],
                                               labels[19]: res[2][idx][5],
                                               labels[20]: res[2][idx][6],
                                               labels[21]: res[2][idx][7]})

    df.to_csv(file_folder + "geneticExchangeTest1.csv")

def retrieve_geneticExchangeTest1(file_folder):
    df = pd.read_csv(file_folder + "geneticExchangeTest1.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[4:8]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[11:15]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[18:22]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Genetic Exchange", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Active Uptake: 5", "Passive Uptake: 4", "Active Metabolism: 2", "Passive Metabolism: 1"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_geneticExchangeTest1__t1(file_folder):
    df = pd.read_csv(file_folder + "geneticExchangeTest1.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[4:8]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Genetic Exchange - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Active Uptake: 5", "Passive Uptake: 4", "Active Metabolism: 2", "Passive Metabolism: 1"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_geneticExchangeTest1("DataCollection/")
retrieve_geneticExchangeTest1("DataCollection/")
retrieve_geneticExchangeTest1__t1("DataCollection/")


def save_geneticExchangeTest2(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism_active = Organism(100, 200, lambda x : 2/4 * x**(2/3), lambda x : 1/20 * x, "active")
        organism_passive = Organism(100, 200, lambda x : 1/4 * x**(2/3), lambda x : 1/50 * x, "passive")
        active_uptake_original = organism_active.uptake_rate(1)
        active_metabolite_original = organism_active.uptake_rate(1)
        environment1 = Environment(10**3, 1000, [organism_active, organism_passive])
        labels.append("population_active" + "__t" + str(trial+1))
        labels.append("population_passive" + "__t" + str(trial+1))
        labels.append("population_total" + "__t" + str(trial+1))
        labels.append("uptake_active" + "__t" + str(trial+1))
        labels.append("uptake_passive" + "__t" + str(trial+1))
        labels.append("metabolic_active" + "__t" + str(trial+1))
        labels.append("metabolic_passive" + "__t" + str(trial+1))
        items = []
        items.append([0, 1, 1, 2, 1, 1, 1, 1])

        for num in range(2*10**3):
            environment1.update()
            active = 0
            passive = 0
            attributes = {"up_active": 0, "up_passive": 0, "me_active": 0, "me_passive": 0}
            for organism in environment1.population:
                if organism.species == "active":
                    active += 1
                elif organism.species == "passive":
                    passive += 1
                if organism.uptake_rate(1) == active_uptake_original:
                    attributes["up_active"] = attributes["up_active"] + 1
                else:
                    attributes["up_passive"] = attributes["up_passive"] + 1
                if organism.metabolic_rate(1) == active_metabolite_original:
                    attributes["me_active"] = attributes["me_active"] + 1
                else:
                    attributes["me_passive"] = attributes["me_passive"] + 1
            assert((active+passive) == len(environment1.population))
            items.append([num+1, active, passive, active+passive, attributes["up_active"], attributes["up_passive"], attributes["me_active"], attributes["me_passive"]])
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
                                               labels[7]: res[0][idx][7],
                                               labels[8]: res[1][idx][1],
                                               labels[9]: res[1][idx][2],
                                               labels[10]: res[1][idx][3],
                                               labels[11]: res[1][idx][4],
                                               labels[12]: res[1][idx][5],
                                               labels[13]: res[1][idx][6],
                                               labels[14]: res[1][idx][7],
                                               labels[15]: res[2][idx][1],
                                               labels[16]: res[2][idx][2],
                                               labels[17]: res[2][idx][3],
                                               labels[18]: res[2][idx][4],
                                               labels[19]: res[2][idx][5],
                                               labels[20]: res[2][idx][6],
                                               labels[21]: res[2][idx][7]})

    df.to_csv(file_folder + "geneticExchangeTest2.csv")

def retrieve_geneticExchangeTest2(file_folder):
    df = pd.read_csv(file_folder + "geneticExchangeTest2.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[4:8]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[11:15]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[18:22]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Genetic Exchange", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Active Uptake: 2/4 * x**(2/3)", "Passive Uptake: 1/4 * x**(2/3)", "Active Metabolism: 1/20 * x", "Passive Metabolism: 1/50 * x"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_geneticExchangeTest2__t1(file_folder):
    df = pd.read_csv(file_folder + "geneticExchangeTest2.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[4:8]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Genetic Exchange - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Active Uptake: 2/4 * x**(2/3)", "Passive Uptake: 1/4 * x**(2/3)", "Active Metabolism: 1/20 * x", "Passive Metabolism: 1/50 * x"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_geneticExchangeTest2("DataCollection/")
retrieve_geneticExchangeTest2("DataCollection/")
retrieve_geneticExchangeTest2__t1("DataCollection/")
