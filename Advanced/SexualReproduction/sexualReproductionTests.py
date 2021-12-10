from sexualReproduction import Organism, Environment
import matplotlib.pyplot as plt
import pandas as pd


def save_sexualReproductionTest1(file_folder):
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
        organism_active = Organism(100, 200, lambda x : 5, lambda x : 2, 10000, "active")
        organism_passive = Organism(100, 200, lambda x : 5, lambda x : 2, 10000, "passive")
        environment1 = Environment(1000, 10, [organism_active, organism_passive])
        environment2 = Environment(1000, 100, [organism_active, organism_passive])
        environment3 = Environment(1000, 500, [organism_active, organism_passive])
        labels.append("population_env1" + "__t" + str(trial+1))
        labels.append("population_env2" + "__t" + str(trial+1))
        labels.append("population_env3" + "__t" + str(trial+1))
        items = []
        items.append([0, 2, 2, 2])
        for num in range(10*10**3):
            environment1.update()
            environment2.update()
            environment3.update()
            items.append([num+1, len(environment1.population), len(environment2.population),  len(environment3.population)])
        res.append(items)

    # An empty dataframe with the labels and an appropriate number of entries
    # is created and then filled with the corresponding values.
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

    # The dataframe is stored as a csv file.
    df.to_csv(file_folder + "sexualReproductionTest1.csv")

def retrieve_sexualReproductionTest1(file_folder):
    """
    This function retrieves the results from this test from a csv file and
    plots all trials.
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "sexualReproductionTest1.csv", index_col=0)

    # An empty plot with subplots is created and formating attributes are
    # defined.
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    # The subplots are filled with the corresponding data.
    for column in df.columns[1:4]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[4:7]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[7:10]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    # The plot is labeled properly.
    axes[0].set_title("Sexual Reproduction (age limit: 10'000)", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Environment 1 (refill: 10)", "Environment 2 (refill: 100)", "Environment 3 (refill: 500)"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_sexualReproductionTest1__t1(file_folder):
    """
    This function retrieves the results from this test from a csv file and
    plots only one trial.
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "sexualReproductionTest1.csv", index_col=0)

    # An empty plot with one subplot is created and formatting attributes are
    # defined.
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    # The subplot is filled with the corresponding data.
    for column in df.columns[1:4]:
        df[column].plot(ax=axes, x=df.columns[0])

    # The plot is labeled properly.
    axes.set_title("Sexual Reproduction (age limit: 10'000) - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Environment 1 (refill: 10)", "Environment 2 (refill: 100)", "Environment 3 (refill: 500)"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_sexualReproductionTest1("DataCollection/")
retrieve_sexualReproductionTest1("DataCollection/")
retrieve_sexualReproductionTest1__t1("DataCollection/")


def save_sexualReproductionTest2(file_folder):
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
        organism_active_100 = Organism(100, 200, lambda x : 5, lambda x : 2, 100, "active")
        organism_passive_100 = Organism(100, 200, lambda x : 5, lambda x : 2, 100, "passive")
        organism_active_300 = Organism(100, 200, lambda x : 5, lambda x : 2, 300, "active")
        organism_passive_300 = Organism(100, 200, lambda x : 5, lambda x : 2, 300, "passive")
        organism_active_500 = Organism(100, 200, lambda x : 5, lambda x : 2, 500, "active")
        organism_passive_500 = Organism(100, 200, lambda x : 5, lambda x : 2, 500, "passive")
        environment1 = Environment(1000, 500, [organism_active_100, organism_passive_100])
        environment2 = Environment(1000, 500, [organism_active_300, organism_passive_300])
        environment3 = Environment(1000, 500, [organism_active_500, organism_passive_500])
        labels.append("population_env1" + "__t" + str(trial+1))
        labels.append("population_env2" + "__t" + str(trial+1))
        labels.append("population_env3" + "__t" + str(trial+1))
        items = []
        items.append([0, 2, 2, 2])
        for num in range(10*10**3):
            environment1.update()
            environment2.update()
            environment3.update()
            items.append([num+1, len(environment1.population), len(environment2.population),  len(environment3.population)])
        res.append(items)

    # An empty dataframe with the labels and an appropriate number of entries
    # is created and then filled with the corresponding values.
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

    # The dataframe is stored as a csv file.
    df.to_csv(file_folder + "sexualReproductionTest2.csv")

def retrieve_sexualReproductionTest2(file_folder):
    """
    This function retrieves the results from this test from a csv file and
    plots all trials.
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "sexualReproductionTest2.csv", index_col=0)

    # An empty plot with subplots is created and formating attributes are
    # defined.
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    # The subplots are filled with the corresponding data.
    for column in df.columns[1:4]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[4:7]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[7:10]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    # The plot is labeled properly.
    axes[0].set_title("Sexual Reproduction (refill: 500)", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["organisms 1 (age limit:100))", "organisms 2 (age limit: 300)", "organisms 3 (age limit: 500)"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_sexualReproductionTest2__t2(file_folder):
    """
    This function retrieves the results from this test from a csv file and
    plots only one trial.
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "sexualReproductionTest2.csv", index_col=0)

    # An empty plot with one subplot is created and formatting attributes are
    # defined.
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    # The subplot is filled with the corresponding data.
    for column in df.columns[4:7]:
        df[column].plot(ax=axes, x=df.columns[0])

    # The plot is labeled properly.
    axes.set_title("Sexual Reproduction (refill: 500) - Trial 2", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["organisms 1 (age limit:100))", "organisms 2 (age limit: 300)", "organisms 3 (age limit: 500)"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_sexualReproductionTest2("DataCollection/")
retrieve_sexualReproductionTest2("DataCollection/")
retrieve_sexualReproductionTest2__t2("DataCollection/")


def save_sexualReproductionTest3(file_folder):
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
        organism1 = Organism(100 , 200, lambda x: 5, lambda x: 2, 300, "active")
        organism2 = Organism(100 , 200, lambda x: 5, lambda x: 2, 300, "passive")
        environment1 = Environment(1000, 500, [organism1, organism2])
        labels.append("population_size" + "__t" + str(trial+1))
        labels.append("available_food" + "__t" + str(trial+1))
        items = []
        items.append([0, 2, environment1.food])
        for num in range(2*10**3):
            environment1.update()
            items.append([num+1, len(environment1.population), environment1.food])
        res.append(items)

    # An empty dataframe with the labels and an appropriate number of entries
    # is created and then filled with the corresponding values.
    df = pd.DataFrame(columns=labels, index=range(len(res[0])))
    for idx, item in enumerate(res[0]):
        df.loc[idx] = pd.Series({labels[0]: res[0][idx][0],
                                               labels[1]: res[0][idx][1],
                                               labels[2]: res[0][idx][2],
                                               labels[3]: res[1][idx][1],
                                               labels[4]: res[1][idx][2],
                                               labels[5]: res[2][idx][1],
                                               labels[6]: res[2][idx][2]})

    # The dataframe is stored as a csv file.
    df.to_csv(file_folder + "sexualReproductionTest3.csv")

def retrieve_sexualReproductionTest3(file_folder):
    """
    This function retrieves the results from this test from a csv file and
    plots all trials.
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "sexualReproductionTest3.csv", index_col=0)

    # An empty plot with subplots is created and formating attributes are
    # defined.
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1)
    lbl_ax = axes[1].twinx()

    # The subplots are filled with the corresponding data.
    df["population_size__t1"].plot(ax=axes[0], x=df["cycle"], color=plt.rcParams['axes.prop_cycle'].by_key()['color'][0])
    df["available_food__t1"].plot(ax=axes[0].twinx(), x=df["cycle"], color=plt.rcParams['axes.prop_cycle'].by_key()['color'][1])
    df["population_size__t2"].plot(ax=axes[1], x=df["cycle"], color=plt.rcParams['axes.prop_cycle'].by_key()['color'][0])
    df["available_food__t2"].plot(ax=lbl_ax, x=df["cycle"], color=plt.rcParams['axes.prop_cycle'].by_key()['color'][1])
    df["population_size__t1"].plot(ax=axes[2], x=df["cycle"], color=plt.rcParams['axes.prop_cycle'].by_key()['color'][0])
    df["available_food__t3"].plot(ax=axes[2].twinx(), x=df["cycle"], color=plt.rcParams['axes.prop_cycle'].by_key()['color'][1])

    # The plot is labeled properly.
    axes[0].set_title("Sexual Reproduction (refill: 500, age limit: 300)", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[1].set_ylabel("Population Size", color = plt.rcParams['axes.prop_cycle'].by_key()['color'][0], fontsize=14)
    lbl_ax.set_ylabel("Availabe Food", color = plt.rcParams['axes.prop_cycle'].by_key()['color'][1], fontsize=14)

    plt.show

def retrieve_sexualReproductionTest3__t1(file_folder):
    """
    This function retrieves the results from this test from a csv file and
    plots only one trial.
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "sexualReproductionTest3.csv", index_col=0)

    # An empty plot with one subplot is created and formatting attributes are
    # defined.
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig,ax = plt.subplots()

    # The subplot is filled with the corresponding data and labeled properly.
    ax.plot(df["cycle"].to_list(), df["population_size__t1"].to_list(), color= plt.rcParams['axes.prop_cycle'].by_key()['color'][0], marker=".")
    ax.set_xlabel("Time", fontsize=14)
    ax.set_ylabel("Population Size",  color = plt.rcParams['axes.prop_cycle'].by_key()['color'][0], fontsize=14)
    ax.set_title("Sexual Reproduction (refill: 500, age limit: 300) - Trial 1", fontsize = 18)
    ax2 = ax.twinx()
    ax2.plot(df["cycle"].to_list(), df["available_food__t1"].to_list(), color =  plt.rcParams['axes.prop_cycle'].by_key()['color'][1], marker=".")
    ax2.set_ylabel("Availabe Food", color =  plt.rcParams['axes.prop_cycle'].by_key()['color'][1], fontsize=14)
    plt.show()

save_sexualReproductionTest3("DataCollection/")
retrieve_sexualReproductionTest3("DataCollection/")
retrieve_sexualReproductionTest3__t1("DataCollection/")
