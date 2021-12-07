from basicOrganismsAndEnvironment import Organism, Environment
import matplotlib.pyplot as plt
import pandas as pd


##############
# Organism Tests
##############
"""
CHANGE THESE TO LAWS THAT MAKE SENSE FOR A CERTAIN GEOMETRY --> disks, spheres, ...
"""
def basicTest_variableSize(file_folder=None):
    res = []
    labels = []

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 1/4 * x**(2/3), lambda x : 1/50 * x, "Specimen One")
        organism2 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen Two")
        labels.append("cycle" + "__t" + str(trial+1))
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
                                               labels[3]: res[1][idx][0],
                                               labels[4]: res[1][idx][1],
                                               labels[5]: res[1][idx][2],
                                               labels[6]: res[2][idx][0],
                                               labels[7]: res[2][idx][1],
                                               labels[8]: res[2][idx][2]})


    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:3]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[4:6]:
        df[column].plot(ax=axes[1], x=df.columns[3])
    for column in df.columns[7:9]:
        df[column].plot(ax=axes[2], x=df.columns[6], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

    df
    # df.to_csv(file_folder + "_basicTest_variableSize.csv")
    # df = pd.read_csv(file_folder + "_basicTest_variableSize.csv", index_col=0)


#################
# Environment Tests
#################
def basicTest_Environment1(file_folder=None):
    res = []
    labels = []

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(10**3, 100, [organism1])
        labels.append("cycle" + "__t" + str(trial+1))
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
                                               labels[2]: res[1][idx][0],
                                               labels[3]: res[1][idx][1],
                                               labels[4]: res[2][idx][0],
                                               labels[5]: res[2][idx][1]})

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[1], x=df.columns[2])
    for column in df.columns[5:6]:
        df[column].plot(ax=axes[2], x=df.columns[4], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

    df
    #df.to_csv(file_folder + "_basicTest_Environment1.csv")
    # df = pd.read_csv(file_folder + "_basicTest_Environment1.csv", index_col=0)

def basicTest_Environment2(file_folder=None):
    res = []
    labels = []

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(10**3, 100, [organism1])
        labels.append("cycle" + "__t" + str(trial+1))
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
                                               labels[2]: res[1][idx][0],
                                               labels[3]: res[1][idx][1],
                                               labels[4]: res[2][idx][0],
                                               labels[5]: res[2][idx][1]})

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[1], x=df.columns[2])
    for column in df.columns[5:6]:
        df[column].plot(ax=axes[2], x=df.columns[4], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

    df
    #df.to_csv(file_folder + "_basicTest_Environment2.csv")
    # df = pd.read_csv(file_folder + "_basicTest_Environment2.csv", index_col=0)

def basicTest_Environment3(file_folder=None):
    res = []
    labels = []

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(10**3, 100, [organism1])
        labels.append("cycle" + "__t" + str(trial+1))
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
                                               labels[2]: res[1][idx][0],
                                               labels[3]: res[1][idx][1],
                                               labels[4]: res[2][idx][0],
                                               labels[5]: res[2][idx][1]})

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[1], x=df.columns[2])
    for column in df.columns[5:6]:
        df[column].plot(ax=axes[2], x=df.columns[4], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

    df
    #df.to_csv(file_folder + "_basicTest_Environment3.csv")
    # df = pd.read_csv(file_folder + "_basicTest_Environment3.csv", index_col=0)

def basicTest_Environment4(file_folder=None):
    res = []
    labels = []

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(10**3, 10**3, [organism1])
        labels.append("cycle" + "__t" + str(trial+1))
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
                                               labels[2]: res[1][idx][0],
                                               labels[3]: res[1][idx][1],
                                               labels[4]: res[2][idx][0],
                                               labels[5]: res[2][idx][1]})

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[1], x=df.columns[2])
    for column in df.columns[5:6]:
        df[column].plot(ax=axes[2], x=df.columns[4], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

    df
    #df.to_csv(file_folder + "_basicTest_Environment4.csv")
    # df = pd.read_csv(file_folder + "_basicTest_Environment4.csv", index_col=0)

def basicTest_Environment5(file_folder=None):
    res = []
    labels = []

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(10**3, 10**3, [organism1])
        labels.append("cycle" + "__t" + str(trial+1))
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
                                               labels[2]: res[1][idx][0],
                                               labels[3]: res[1][idx][1],
                                               labels[4]: res[2][idx][0],
                                               labels[5]: res[2][idx][1]})

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[1], x=df.columns[2])
    for column in df.columns[5:6]:
        df[column].plot(ax=axes[2], x=df.columns[4], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

    df
    #df.to_csv(file_folder + "_basicTest_Environment5.csv")
    # df = pd.read_csv(file_folder + "_basicTest_Environment5.csv", index_col=0)

"""
Or refill = 10**3 and food = 0 (p. 9-10 from artificial_life.pdf)
"""
def basicTest_Environment6(file_folder=None):
    res = []
    labels = []

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(0, 100, [organism1])
        labels.append("cycle" + "__t" + str(trial+1))
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
                                               labels[2]: res[1][idx][0],
                                               labels[3]: res[1][idx][1],
                                               labels[4]: res[2][idx][0],
                                               labels[5]: res[2][idx][1]})

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[1], x=df.columns[2])
    for column in df.columns[5:6]:
        df[column].plot(ax=axes[2], x=df.columns[4], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

    df
    #df.to_csv(file_folder + "_basicTest_Environment6.csv")
    # df = pd.read_csv(file_folder + "_basicTest_Environment6.csv", index_col=0)

"""
Or refill = 10**3 and food = 0 (p. 9-10 from artificial_life.pdf)
"""
def basicTest_Environment7(file_folder=None):
    res = []
    labels = []

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(0, 100, [organism1])
        labels.append("cycle" + "__t" + str(trial+1))
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
                                               labels[2]: res[1][idx][0],
                                               labels[3]: res[1][idx][1],
                                               labels[4]: res[2][idx][0],
                                               labels[5]: res[2][idx][1]})

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[1], x=df.columns[2])
    for column in df.columns[5:6]:
        df[column].plot(ax=axes[2], x=df.columns[4], label=column[:column.find("__t")])

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show

    df
    #df.to_csv(file_folder + "_basicTest_Environment7.csv")
    # df = pd.read_csv(file_folder + "_basicTest_Environment7.csv", index_col=0)
