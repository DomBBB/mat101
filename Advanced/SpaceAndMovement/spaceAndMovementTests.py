from spaceAndMovement import Organism, Environment
import matplotlib.pyplot as plt
import pandas as pd
import copy
import json


def save_spaceAndMovementTest1(file_folder):
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
        organism_active = Organism(100, 200, lambda x : 3, lambda x : 1, "active")
        organism_passive = Organism(100, 200, lambda x : 3, lambda x : 1, "passive")
        environment1 = Environment(100, 10, [organism_active, organism_passive], 5)
        labels.append("population_active" + "__t" + str(trial+1))
        labels.append("population_passive" + "__t" + str(trial+1))
        labels.append("population_total" + "__t" + str(trial+1))
        labels.append("food_crates" + "__t" + str(trial+1))
        labels.append("organism_positions" + "__t" + str(trial+1))
        items = []
        items.append([0, 1, 1, 2, copy.deepcopy(environment1.food_crates), [[organism_active.organism_position[0], organism_active.organism_position[1], organism_active.species], [organism_passive.organism_position[0], organism_passive.organism_position[1], organism_passive.species]]])
        for num in range(2*10**3):
            environment1.update()
            active = 0
            passive = 0
            positions = []
            for organism in environment1.population:
                if organism.species == "active":
                    active += 1
                elif organism.species == "passive":
                    passive += 1
                positions.append([organism.organism_position[0], organism.organism_position[1], organism.species])
            assert((active+passive) == len(environment1.population))
            items.append([num+1, active, passive, active+passive, copy.deepcopy(environment1.food_crates), positions])
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
                                               labels[6]: res[1][idx][1],
                                               labels[7]: res[1][idx][2],
                                               labels[8]: res[1][idx][3],
                                               labels[9]: res[1][idx][4],
                                               labels[10]: res[1][idx][5],
                                               labels[11]: res[2][idx][1],
                                               labels[12]: res[2][idx][2],
                                               labels[13]: res[2][idx][3],
                                               labels[14]: res[2][idx][4],
                                               labels[15]: res[2][idx][5]})

    # The dataframe is stored as a csv file.
    df.to_csv(file_folder + "spaceAndMovementTest1.csv")

def retrieve_spaceAndMovementTest1(file_folder):
    """
    This function retrieves the results from this test from a csv file and
    plots all trials.
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "spaceAndMovementTest1.csv", index_col=0)

    # An empty plot with subplots is created and formating attributes are
    # defined.
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    # The subplots are filled with the corresponding data.
    for column in df.columns[1:4]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[6:9]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[11:14]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    # The plot is labeled properly.
    axes[0].set_title("Space And Movement", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Active: 3 & 1", "Passive: 3 & 1", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_spaceAndMovementTest1__t1(file_folder):
    """
    This function retrieves the results from this test from a csv file and
    plots only one trial.
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "spaceAndMovementTest1.csv", index_col=0)

    # An empty plot with one subplot is created and formatting attributes are
    # defined.
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    # The subplot is filled with the corresponding data.
    for column in df.columns[1:4]:
        df[column].plot(ax=axes, x=df.columns[0])

    # The plot is labeled properly.
    axes.set_title("Space And Movement - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Active: 3 & 1", "Passive: 3 & 1", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def draw_spaceAndMovementTest1(file_folder, lower, upper, cycle):
    """
    This function retrieves the results from this test from a csv file and
    draws a map of one trial (cycle argument) for the time-steps between
    lower and upper (arguments)
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "spaceAndMovementTest1.csv", index_col=0)

    # Loops through lower-upper to draw only
    # those time-steps. In each iteration an entry is selected and the food
    # crates are drawn in green, active organisms in red and passive
    # organisms in blue.
    for i in range(lower, upper):
        lst_crate = json.loads(df["food_crates__"+cycle].iloc[i])
        crate_x = [x for x, y, z in lst_crate]
        crate_y = [y for x, y, z in lst_crate]
        crate_amount = [z for x, y, z in lst_crate]
        plt.scatter(crate_x, crate_y, s=crate_amount, c="green")
        stringified = df["organism_positions__"+cycle].iloc[i].replace("active", "0").replace( "passive", "1"). replace("'", "")
        lst_organisms = json.loads(stringified)
        org_x = [x for x, y, z in lst_organisms]
        org_y = [y for x, y, z in lst_organisms]
        org_color = ["red" if z==0 else "blue" for x, y, z in lst_organisms]
        plt.scatter(org_x, org_y, c=org_color)
        plt.xlim([0, 50])
        plt.ylim([0, 50])
        plt.show()

save_spaceAndMovementTest1("DataCollection/")
retrieve_spaceAndMovementTest1("DataCollection/")
retrieve_spaceAndMovementTest1__t1("DataCollection/")
draw_spaceAndMovementTest1("DataCollection/", 0, 100, "t1")


def save_spaceAndMovementTest2(file_folder):
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
        organism_active = Organism(100, 200, lambda x : 5, lambda x : 3, "active")
        organism_passive = Organism(100, 200, lambda x : 4, lambda x : 1, "passive")
        environment1 = Environment(100, 10, [organism_active, organism_passive], 5)
        labels.append("population_active" + "__t" + str(trial+1))
        labels.append("population_passive" + "__t" + str(trial+1))
        labels.append("population_total" + "__t" + str(trial+1))
        labels.append("food_crates" + "__t" + str(trial+1))
        labels.append("organism_positions" + "__t" + str(trial+1))
        items = []
        items.append([0, 1, 1, 2, copy.deepcopy(environment1.food_crates), [[organism_active.organism_position[0], organism_active.organism_position[1], organism_active.species], [organism_passive.organism_position[0], organism_passive.organism_position[1], organism_passive.species]]])
        for num in range(2*10**3):
            environment1.update()
            active = 0
            passive = 0
            positions = []
            for organism in environment1.population:
                if organism.species == "active":
                    active += 1
                elif organism.species == "passive":
                    passive += 1
                positions.append([organism.organism_position[0], organism.organism_position[1], organism.species])
            assert((active+passive) == len(environment1.population))
            items.append([num+1, active, passive, active+passive, copy.deepcopy(environment1.food_crates), positions])
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
                                               labels[6]: res[1][idx][1],
                                               labels[7]: res[1][idx][2],
                                               labels[8]: res[1][idx][3],
                                               labels[9]: res[1][idx][4],
                                               labels[10]: res[1][idx][5],
                                               labels[11]: res[2][idx][1],
                                               labels[12]: res[2][idx][2],
                                               labels[13]: res[2][idx][3],
                                               labels[14]: res[2][idx][4],
                                               labels[15]: res[2][idx][5]})

    # The dataframe is stored as a csv file.
    df.to_csv(file_folder + "spaceAndMovementTest2.csv")

def retrieve_spaceAndMovementTest2(file_folder):
    """
    This function retrieves the results from this test from a csv file and
    plots all trials.
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "spaceAndMovementTest2.csv", index_col=0)

    # An empty plot with subplots is created and formating attributes are
    # defined.
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    # The subplots are filled with the corresponding data.
    for column in df.columns[1:4]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[6:9]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[11:14]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    # The plot is labeled properly.
    axes[0].set_title("Space And Movement", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Active: 5 & 3", "Passive: 4 & 1", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_spaceAndMovementTest2__t1(file_folder):
    """
    This function retrieves the results from this test from a csv file and
    plots only one trial.
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "spaceAndMovementTest2.csv", index_col=0)

    # An empty plot with one subplot is created and formatting attributes are
    # defined.
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    # The subplot is filled with the corresponding data.
    for column in df.columns[1:4]:
        df[column].plot(ax=axes, x=df.columns[0])

    # The plot is labeled properly.
    axes.set_title("Space And Movement - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Active: 5 & 3", "Passive: 4 & 1", "Total Population"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def draw_spaceAndMovementTest2(file_folder, lower, upper, cycle):
    """
    This function retrieves the results from this test from a csv file and
    draws a map of one trial (cycle argument) for the time-steps between
    lower and upper (arguments)
    """
    # The dataframe is retrieved from a csv file.
    df = pd.read_csv(file_folder + "spaceAndMovementTest2.csv", index_col=0)

    # Loops through lower-upper to draw only
    # those time-steps. In each iteration an entry is selected and the food
    # crates are drawn in green, active organisms in red and passive
    # organisms in blue.
    for i in range(lower, upper):
        lst_crate = json.loads(df["food_crates__"+cycle].iloc[i])
        crate_x = [x for x, y, z in lst_crate]
        crate_y = [y for x, y, z in lst_crate]
        crate_amount = [z for x, y, z in lst_crate]
        plt.scatter(crate_x, crate_y, s=crate_amount, c="green")
        stringified = df["organism_positions__"+cycle].iloc[i].replace("active", "0").replace( "passive", "1"). replace("'", "")
        lst_organisms = json.loads(stringified)
        org_x = [x for x, y, z in lst_organisms]
        org_y = [y for x, y, z in lst_organisms]
        org_color = ["red" if z==0 else "blue" for x, y, z in lst_organisms]
        plt.scatter(org_x, org_y, c=org_color)
        plt.xlim([0, 50])
        plt.ylim([0, 50])
        plt.show()

save_spaceAndMovementTest2("DataCollection/")
retrieve_spaceAndMovementTest2("DataCollection/")
retrieve_spaceAndMovementTest2__t1("DataCollection/")
draw_spaceAndMovementTest2("DataCollection/", 190, 210, "t1")
