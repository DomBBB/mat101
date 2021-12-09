from OrganismsMetabolite import Organism, Environment
import matplotlib.pyplot as plt
import pandas as pd


def save_metaboliteTest1(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism_active = Organism(100, 200, lambda x : 5, lambda x : 2, lambda x: 0.5*x, "active")
        organism_passive = Organism(100, 200, lambda x : 3, lambda x : 1, lambda x: 1*x, "passive")
        environment1 = Environment(10**3, 10**3, [organism_active, organism_passive], 1) # 1 = metabolites are not reduced by environment
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
                                               labels[4]: res[1][idx][1],
                                               labels[5]: res[1][idx][2],
                                               labels[6]: res[1][idx][3],
                                               labels[7]: res[2][idx][1],
                                               labels[8]: res[2][idx][2],
                                               labels[9]: res[2][idx][3]})

    df.to_csv(file_folder + "metaboliteTest1.csv")

def retrieve_metaboliteTest1(file_folder):
    df = pd.read_csv(file_folder + "metaboliteTest1.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:4]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[4:7]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[7:10]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Metabolite Production (discard none)", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Active: 5, 2, 0.5*x", "Passive: 3, 1, 1*x", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_metaboliteTest1__t1(file_folder):
    df = pd.read_csv(file_folder + "metaboliteTest1.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:4]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Metabolite Production (discard none) - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Active: 5, 2, 0.5*x", "Passive: 3, 1, 1*x", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_metaboliteTest1("DataCollection/")
retrieve_metaboliteTest1("DataCollection/")
retrieve_metaboliteTest1__t1("DataCollection/")


def save_metaboliteTest2(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism_active = Organism(100, 200, lambda x : 5, lambda x : 2, lambda x: 0.5*x, "active")
        organism_passive = Organism(100, 200, lambda x : 3, lambda x : 1, lambda x: 1*x, "passive")
        environment1 = Environment(10**3, 10**3, [organism_active, organism_passive], 0.8) # 1 = metabolites are not reduced by environment
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
                                               labels[4]: res[1][idx][1],
                                               labels[5]: res[1][idx][2],
                                               labels[6]: res[1][idx][3],
                                               labels[7]: res[2][idx][1],
                                               labels[8]: res[2][idx][2],
                                               labels[9]: res[2][idx][3]})

    df.to_csv(file_folder + "metaboliteTest2.csv")

def retrieve_metaboliteTest2(file_folder):
    df = pd.read_csv(file_folder + "metaboliteTest2.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:4]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[4:7]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[7:10]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Metabolite Production (discard 20%)", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Active: 5, 2, 0.5*x", "Passive: 3, 1, 1*x", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_metaboliteTest2__t1(file_folder):
    df = pd.read_csv(file_folder + "metaboliteTest2.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:4]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Metabolite Production (discard 20%) - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Active: 5, 2, 0.5*x", "Passive: 3, 1, 1*x", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_metaboliteTest2("DataCollection/")
retrieve_metaboliteTest2("DataCollection/")
retrieve_metaboliteTest2__t1("DataCollection/")


def save_metaboliteTest3(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism_active = Organism(100, 200, lambda x : 2, lambda x : 1, lambda x: 1*x, "active")
        organism_passive = Organism(100, 200, lambda x : 2, lambda x : 1, lambda x: 1*x, "passive")
        environment1 = Environment(10**3, 10**3, [organism_active, organism_passive], 0.8) # 1 = metabolites are not reduced by environment
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
                                               labels[4]: res[1][idx][1],
                                               labels[5]: res[1][idx][2],
                                               labels[6]: res[1][idx][3],
                                               labels[7]: res[2][idx][1],
                                               labels[8]: res[2][idx][2],
                                               labels[9]: res[2][idx][3]})

    df.to_csv(file_folder + "metaboliteTest3.csv")

def retrieve_metaboliteTest3(file_folder):
    df = pd.read_csv(file_folder + "metaboliteTest3.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:4]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[4:7]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[7:10]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Metabolite Production (discard 20%)", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Active: 2, 1, 1*x", "Passive: 2, 1, 1*x", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_metaboliteTest3__t1(file_folder):
    df = pd.read_csv(file_folder + "metaboliteTest3.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:4]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Metabolite Production (discard 20%) - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Active: 2, 1, 1*x", "Passive: 2, 1, 1*x", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_metaboliteTest3("DataCollection/")
retrieve_metaboliteTest3("DataCollection/")
retrieve_metaboliteTest3__t1("DataCollection/")


def save_metaboliteTest4(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism_active = Organism(100, 200, lambda x : 2, lambda x : 1, lambda x: 0, "excreter")
        organism_passive = Organism(100, 200, lambda x : 2, lambda x : 1, lambda x: 1*x, "passive")
        environment1 = Environment(10**3, 10**3, [organism_active, organism_passive], 0.8) # 1 = metabolites are not reduced by environment
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
                if organism.species == "excreter":
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
                                               labels[4]: res[1][idx][1],
                                               labels[5]: res[1][idx][2],
                                               labels[6]: res[1][idx][3],
                                               labels[7]: res[2][idx][1],
                                               labels[8]: res[2][idx][2],
                                               labels[9]: res[2][idx][3]})

    df.to_csv(file_folder + "metaboliteTest4.csv")

def retrieve_metaboliteTest4(file_folder):
    df = pd.read_csv(file_folder + "metaboliteTest4.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:4]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[4:7]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[7:10]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Metabolite Production (discard 20%)", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Excreter: 2, 1, 0", "Passive: 2, 1, 1*x", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_metaboliteTest4__t1(file_folder):
    df = pd.read_csv(file_folder + "metaboliteTest4.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:4]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Metabolite Production (discard 20%) - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Excreter: 2, 1, 0", "Passive: 2, 1, 1*x", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_metaboliteTest4("DataCollection/")
retrieve_metaboliteTest4("DataCollection/")
retrieve_metaboliteTest4__t1("DataCollection/")


def save_metaboliteTest5(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism_active = Organism(100, 200, lambda x : 4, lambda x : 2, lambda x: 0, "excreter")
        organism_passive = Organism(100, 200, lambda x : 2, lambda x : 1, lambda x: 1*x, "passive")
        environment1 = Environment(10**3, 10**3, [organism_active, organism_passive], 0.8) # 1 = metabolites are not reduced by environment
        labels.append("population_active" + "__t" + str(trial+1))
        labels.append("population_passive" + "__t" + str(trial+1))
        labels.append("population_total" + "__t" + str(trial+1))
        items = []
        items.append([0, 1, 1, 2])

        for num in range(3*10**3):
            environment1.update()
            active = 0
            passive = 0
            for organism in environment1.population:
                if organism.species == "excreter":
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
                                               labels[4]: res[1][idx][1],
                                               labels[5]: res[1][idx][2],
                                               labels[6]: res[1][idx][3],
                                               labels[7]: res[2][idx][1],
                                               labels[8]: res[2][idx][2],
                                               labels[9]: res[2][idx][3]})

    df.to_csv(file_folder + "metaboliteTest5.csv")

def retrieve_metaboliteTest5(file_folder):
    df = pd.read_csv(file_folder + "metaboliteTest5.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:4]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[4:7]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[7:10]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Metabolite Production (discard 20%)", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Excreter: 4, 2, 0", "Passive: 2, 1, 1*x", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_metaboliteTest5__t1(file_folder):
    df = pd.read_csv(file_folder + "metaboliteTest5.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:4]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Metabolite Production (discard 20%) - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Excreter: 4, 2, 0", "Passive: 2, 1, 1*x", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_metaboliteTest5("DataCollection/")
retrieve_metaboliteTest5("DataCollection/")
retrieve_metaboliteTest5__t1("DataCollection/")


def save_metaboliteTest6(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism_active = Organism(100, 200, lambda x : 3, lambda x : 1, lambda x: 0, "excreter")
        organism_passive = Organism(100, 200, lambda x : 2, lambda x : 1, lambda x: 1*x, "passive")
        environment1 = Environment(10**3, 10**3, [organism_active, organism_passive], 0.8) # 1 = metabolites are not reduced by environment
        labels.append("population_active" + "__t" + str(trial+1))
        labels.append("population_passive" + "__t" + str(trial+1))
        labels.append("population_total" + "__t" + str(trial+1))
        items = []
        items.append([0, 1, 1, 2])

        for num in range(10*10**3):
            environment1.update()
            active = 0
            passive = 0
            for organism in environment1.population:
                if organism.species == "excreter":
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
                                               labels[4]: res[1][idx][1],
                                               labels[5]: res[1][idx][2],
                                               labels[6]: res[1][idx][3],
                                               labels[7]: res[2][idx][1],
                                               labels[8]: res[2][idx][2],
                                               labels[9]: res[2][idx][3]})

    df.to_csv(file_folder + "metaboliteTest6.csv")

def retrieve_metaboliteTest6(file_folder):
    df = pd.read_csv(file_folder + "metaboliteTest6.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:4]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[4:7]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[7:10]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Metabolite Production (discard 20%)", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Excreter: 3, 1, 0", "Passive: 2, 1, 1*x", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_metaboliteTest6__t1(file_folder):
    df = pd.read_csv(file_folder + "metaboliteTest6.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:4]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Metabolite Production (discard 20%) - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Excreter: 3, 1, 0", "Passive: 2, 1, 1*x", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_metaboliteTest6("DataCollection/")
retrieve_metaboliteTest6("DataCollection/")
retrieve_metaboliteTest6__t1("DataCollection/")
