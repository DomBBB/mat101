from basicOrganismsAndEnvironment import Organism, Environment
import matplotlib.pyplot as plt
import pandas as pd


##############
# Organism Tests
##############
"""
CHANGE LAMBDA RATES TO OTHER LAWS THAT MAKE SENSE FOR A CERTAIN GEOMETRY --> disks, spheres, ...
"""
def save_basicTest_variableSize(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 1/4 * x**(2/3), lambda x : 1/50 * x, "Specimen One")
        organism2 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Two")
        labels.append("organismsize_variableRate" + "__t" + str(trial+1))
        labels.append("organismsize_fixedRate" + "__t" + str(trial+1))
        items = []
        items.append([0, organism1.size, organism2.size])
        for num in range(1000):
            organism1.update()
            organism2.update()
            items.append([num+1, organism1.size, organism2.size])
        res.append(items)

    # STORE
    df = pd.DataFrame(columns=labels, index=range(len(res[0])))
    for idx, item in enumerate(res[0]):
        df.loc[idx] = pd.Series({labels[0]: res[0][idx][0],
                                               labels[1]: res[0][idx][1],
                                               labels[2]: res[0][idx][2],
                                               labels[3]: res[1][idx][1],
                                               labels[4]: res[1][idx][2],
                                               labels[5]: res[2][idx][1],
                                               labels[6]: res[2][idx][2]})

    df.to_csv(file_folder + "basicTest_variableSize.csv")

def retrieve_basicTest_variableSize(file_folder):
    df = pd.read_csv(file_folder + "basicTest_variableSize.csv", index_col=0)
    print(df)

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:3]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[3:5]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[5:7]:
        df[column].plot(ax=axes[2], x=df.columns[0], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

# save_basicTest_variableSize("DataCollection/")
retrieve_basicTest_variableSize("DataCollection/")


#################
# Environment Tests
#################
"""
Are basicTest_Environment6 & basicTest_Environment7 correct?
"""
def save_basicTest_Environment1(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(10**3, 100, [organism1])
        labels.append("population" + "__t" + str(trial+1))
        items = []
        items.append([0, len(environment1.population)])
        for num in range(100):
            environment1.update()
            items.append([num+1, len(environment1.population)])
        res.append(items)

    # STORE
    df = pd.DataFrame(columns=labels, index=range(len(res[0])))
    for idx, item in enumerate(res[0]):
        df.loc[idx] = pd.Series({labels[0]: res[0][idx][0],
                                               labels[1]: res[0][idx][1],
                                               labels[2]: res[1][idx][1],
                                               labels[3]: res[2][idx][1]})

    df.to_csv(file_folder + "basicTest_Environment1.csv")

def retrieve_basicTest_Environment1(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment1.csv", index_col=0)
    print(df)

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

# save_basicTest_Environment1("DataCollection/")
retrieve_basicTest_Environment1("DataCollection/")


def save_basicTest_Environment2(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(10**3, 100, [organism1])
        labels.append("population" + "__t" + str(trial+1))
        items = []
        items.append([0, len(environment1.population)])
        for num in range(5*10**3):
            environment1.update()
            items.append([num+1, len(environment1.population)])
        res.append(items)

    # STORE
    df = pd.DataFrame(columns=labels, index=range(len(res[0])))
    for idx, item in enumerate(res[0]):
        df.loc[idx] = pd.Series({labels[0]: res[0][idx][0],
                                               labels[1]: res[0][idx][1],
                                               labels[2]: res[1][idx][1],
                                               labels[3]: res[2][idx][1]})

    df.to_csv(file_folder + "basicTest_Environment2.csv")

def retrieve_basicTest_Environment2(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment2.csv", index_col=0)
    print(df)

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

# save_basicTest_Environment2("DataCollection/")
retrieve_basicTest_Environment2("DataCollection/")


def save_basicTest_Environment3(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(10**3, 100, [organism1])
        labels.append("divisions" + "__t" + str(trial+1))
        items = []
        items.append([0, len(environment1.population)])
        for num in range(5*10**3):
            items.append([num+1, environment1.update()])
        res.append(items)

    # STORE
    df = pd.DataFrame(columns=labels, index=range(len(res[0])))
    for idx, item in enumerate(res[0]):
        df.loc[idx] = pd.Series({labels[0]: res[0][idx][0],
                                               labels[1]: res[0][idx][1],
                                               labels[2]: res[1][idx][1],
                                               labels[3]: res[2][idx][1]})

    df.to_csv(file_folder + "basicTest_Environment3.csv")

def retrieve_basicTest_Environment3(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment3.csv", index_col=0)
    print(df)

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

# save_basicTest_Environment3("DataCollection/")
retrieve_basicTest_Environment3("DataCollection/")


def save_basicTest_Environment4(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(10**3, 10**3, [organism1])
        labels.append("population" + "__t" + str(trial+1))
        items = []
        items.append([0, len(environment1.population)])
        for num in range(5*10**3):
            environment1.update()
            items.append([num+1, len(environment1.population)])
        res.append(items)

    # STORE
    df = pd.DataFrame(columns=labels, index=range(len(res[0])))
    for idx, item in enumerate(res[0]):
        df.loc[idx] = pd.Series({labels[0]: res[0][idx][0],
                                               labels[1]: res[0][idx][1],
                                               labels[2]: res[1][idx][1],
                                               labels[3]: res[2][idx][1]})

    df.to_csv(file_folder + "basicTest_Environment4.csv")

def retrieve_basicTest_Environment4(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment4.csv", index_col=0)
    print(df)

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

# save_basicTest_Environment4("DataCollection/")
retrieve_basicTest_Environment4("DataCollection/")


def save_basicTest_Environment5(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(10**3, 10**3, [organism1])
        labels.append("divisions" + "__t" + str(trial+1))
        items = []
        items.append([0, len(environment1.population)])
        for num in range(5*10**3):
            items.append([num+1, environment1.update()])
        res.append(items)

    # STORE
    df = pd.DataFrame(columns=labels, index=range(len(res[0])))
    for idx, item in enumerate(res[0]):
        df.loc[idx] = pd.Series({labels[0]: res[0][idx][0],
                                               labels[1]: res[0][idx][1],
                                               labels[2]: res[1][idx][1],
                                               labels[3]: res[2][idx][1]})

    df.to_csv(file_folder + "basicTest_Environment5.csv")

def retrieve_basicTest_Environment5(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment5.csv", index_col=0)
    print(df)

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

# save_basicTest_Environment5("DataCollection/")
retrieve_basicTest_Environment5("DataCollection/")


"""
Or refill = 10**3 and food = 0 (p. 9-10 from artificial_life.pdf)
"""
def save_basicTest_Environment6(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(0, 100, [organism1])
        labels.append("population" + "__t" + str(trial+1))
        items = []
        items.append([0, len(environment1.population)])
        for num in range(5*10**3):
            environment1.update()
            items.append([num+1, len(environment1.population)])
        res.append(items)

    # STORE
    df = pd.DataFrame(columns=labels, index=range(len(res[0])))
    for idx, item in enumerate(res[0]):
        df.loc[idx] = pd.Series({labels[0]: res[0][idx][0],
                                               labels[1]: res[0][idx][1],
                                               labels[2]: res[1][idx][1],
                                               labels[3]: res[2][idx][1]})

    df.to_csv(file_folder + "basicTest_Environment6.csv")

def retrieve_basicTest_Environment6(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment6.csv", index_col=0)
    print(df)

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

# save_basicTest_Environment6("DataCollection/")
retrieve_basicTest_Environment6("DataCollection/")


"""
Or refill = 10**3 and food = 0 (p. 9-10 from artificial_life.pdf)
"""
def save_basicTest_Environment7(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(0, 100, [organism1])
        labels.append("divisions" + "__t" + str(trial+1))
        items = []
        items.append([0, len(environment1.population)])
        for num in range(5*10**3):
            items.append([num+1, environment1.update()])
        res.append(items)

    # STORE
    df = pd.DataFrame(columns=labels, index=range(len(res[0])))
    for idx, item in enumerate(res[0]):
        df.loc[idx] = pd.Series({labels[0]: res[0][idx][0],
                                               labels[1]: res[0][idx][1],
                                               labels[2]: res[1][idx][1],
                                               labels[3]: res[2][idx][1]})

    df.to_csv(file_folder + "basicTest_Environment7.csv")

def retrieve_basicTest_Environment7(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment7.csv", index_col=0)
    print(df)

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

# save_basicTest_Environment7("DataCollection/")
retrieve_basicTest_Environment7("DataCollection/")
