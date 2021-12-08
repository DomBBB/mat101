from spaceAndMovement import Organism, Environment
import matplotlib.pyplot as plt
import pandas as pd
import copy
import json

"""
CHANGE LAMBDA RATES TO OTHER VALUES TO OBTAIN DIFFERENT GRAPHS
"""
def save_spaceAndMovementTest1(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism_active = Organism(100, 200, lambda x : 3, lambda x : 1, "active") #movement between >0 and 1
        organism_passive = Organism(100, 200, lambda x : 3, lambda x : 1, "passive") #movement between >0 and 1
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

    # STORE
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

    df.to_csv(file_folder + "spaceAndMovementTest1.csv")

def retrieve_spaceAndMovementTest1(file_folder):
    df = pd.read_csv(file_folder + "spaceAndMovementTest1.csv", index_col=0)
    print(df)

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:4]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[6:9]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[11:14]:
        df[column].plot(ax=axes[2], x=df.columns[0], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

    return df

def draw_spaceAndMovementTest1(file_folder, lower, upper, cycle):
    df = pd.read_csv(file_folder + "spaceAndMovementTest1.csv", index_col=0)
    assert(upper-lower <= 30)
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

# save_spaceAndMovementTest1("DataCollection/")
retrieve_spaceAndMovementTest1("DataCollection/")
draw_spaceAndMovementTest1("DataCollection/", 1300, 1318, "t1")
