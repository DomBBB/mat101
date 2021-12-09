from basicOrganismsAndEnvironment import Organism, Environment
import matplotlib.pyplot as plt
import pandas as pd


###############################################################################
# Organism Tests
###############################################################################
def save_basicTest_variableSize1(file_folder):
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

    df.to_csv(file_folder + "basicTest_variableSize1.csv")

def retrieve_basicTest_variableSize1(file_folder):
    df = pd.read_csv(file_folder + "basicTest_variableSize1.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:3]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[3:5]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[5:7]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Size (with unlimited food)", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Variable Rate: 1/4 * x**(2/3) & 1/50 * x", "Fixed Rate: 5 & 2"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_basicTest_variableSize1__t1(file_folder):
    df = pd.read_csv(file_folder + "basicTest_variableSize1.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:3]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Size (with unlimited food) - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Variable Rate: 1/4 * x**(2/3) & 1/50 * x", "Fixed Rate: 5 & 2"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_basicTest_variableSize1("DataCollection/")
retrieve_basicTest_variableSize1("DataCollection/")
retrieve_basicTest_variableSize1__t1("DataCollection/")


def save_basicTest_variableSize2(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 1/2 * x**(2/3), lambda x: 1/30 * x, "Specimen One")
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

    df.to_csv(file_folder + "basicTest_variableSize2.csv")

def retrieve_basicTest_variableSize2(file_folder):
    df = pd.read_csv(file_folder + "basicTest_variableSize2.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:3]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[3:5]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[5:7]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Size (with unlimited food)", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Variable Rate: 1/2 * x**(2/3) & 1/30 * x", "Fixed Rate: 5 & 2"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_basicTest_variableSize2__t1(file_folder):
    df = pd.read_csv(file_folder + "basicTest_variableSize2.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:3]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Size (with unlimited food) - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Variable Rate: 1/2 * x**(2/3) & 1/30 * x", "Fixed Rate: 5 & 2"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_basicTest_variableSize2("DataCollection/")
retrieve_basicTest_variableSize2("DataCollection/")
retrieve_basicTest_variableSize2__t1("DataCollection/")


###############################################################################
# Environment Tests
###############################################################################
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

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Population Size", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Population Size (Food: 1000, Refill: 100)"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_basicTest_Environment1__t1(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment1.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Population Size - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Population Size (Food: 1000, Refill: 100)"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_basicTest_Environment1("DataCollection/")
retrieve_basicTest_Environment1("DataCollection/")
retrieve_basicTest_Environment1__t1("DataCollection/")


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

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Population Size", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Population Size (Food: 1000, Refill: 100)"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_basicTest_Environment2__t1(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment2.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Population Size - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Population Size (Food: 1000, Refill: 100)"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_basicTest_Environment2("DataCollection/")
retrieve_basicTest_Environment2("DataCollection/")
retrieve_basicTest_Environment2__t1("DataCollection/")


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

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Number of divisions", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Number of divisions (Food: 1000, Refill: 100)"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_basicTest_Environment3__t1(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment3.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Number of divisions - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Number of divisions (Food: 1000, Refill: 100)"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_basicTest_Environment3("DataCollection/")
retrieve_basicTest_Environment3("DataCollection/")
retrieve_basicTest_Environment3__t1("DataCollection/")


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

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Population Size", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Population Size (Food: 1000, Refill: 1000)"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_basicTest_Environment4__t1(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment4.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Population Size - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Population Size (Food: 1000, Refill: 1000)"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_basicTest_Environment4("DataCollection/")
retrieve_basicTest_Environment4("DataCollection/")
retrieve_basicTest_Environment4__t1("DataCollection/")


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

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Number of divisions", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Number of divisions (Food: 1000, Refill: 1000)"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_basicTest_Environment5__t1(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment5.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Number of divisions - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Number of divisions (Food: 1000, Refill: 1000)"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_basicTest_Environment5("DataCollection/")
retrieve_basicTest_Environment5("DataCollection/")
retrieve_basicTest_Environment5__t1("DataCollection/")


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

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Population Size", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Population Size (Food: 0, Refill: 100)"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_basicTest_Environment6__t1(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment6.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Population Size - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Population Size (Food: 0, Refill: 100)"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_basicTest_Environment6("DataCollection/")
retrieve_basicTest_Environment6("DataCollection/")
retrieve_basicTest_Environment6__t1("DataCollection/")


def save_basicTest_Environment7(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(0, 1000, [organism1])
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

    df.to_csv(file_folder + "basicTest_Environment7.csv")

def retrieve_basicTest_Environment7(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment7.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Population Size", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Population Size (Food: 0, Refill: 1000)"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_basicTest_Environment7__t1(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment7.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Population Size - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Population Size (Food: 0, Refill: 1000)"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_basicTest_Environment7("DataCollection/")
retrieve_basicTest_Environment7("DataCollection/")
retrieve_basicTest_Environment7__t1("DataCollection/")


def save_basicTest_Environment8(file_folder):
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

    df.to_csv(file_folder + "basicTest_Environment8.csv")

def retrieve_basicTest_Environment8(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment8.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Number of divisions", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Number of divisions (Food: 0, Refill: 100)"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_basicTest_Environment8__t1(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment8.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Number of divisions - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Number of divisions (Food: 0, Refill: 100)"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_basicTest_Environment8("DataCollection/")
retrieve_basicTest_Environment8("DataCollection/")
retrieve_basicTest_Environment8__t1("DataCollection/")


def save_basicTest_Environment9(file_folder):
    res = []
    labels = ["cycle"]

    for trial in range(3):
        organism1 = Organism(100, 200, lambda x : 5, lambda x : 2, "Specimen One")
        environment1 = Environment(0, 1000, [organism1])
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

    df.to_csv(file_folder + "basicTest_Environment9.csv")

def retrieve_basicTest_Environment9(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment9.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes[0], x=df.columns[0])
    for column in df.columns[2:3]:
        df[column].plot(ax=axes[1], x=df.columns[0])
    for column in df.columns[3:4]:
        df[column].plot(ax=axes[2], x=df.columns[0])

    axes[0].set_title("Number of divisions", fontsize = 18)
    axes[2].set_xlabel("Time", fontsize=14)
    axes[2].legend(["Number of divisions (Food: 0, Refill: 1000)"], loc='upper center', bbox_to_anchor=(0.5, -0.6),
          fancybox=True, shadow=True, ncol=5)

    plt.show

def retrieve_basicTest_Environment9__t1(file_folder):
    df = pd.read_csv(file_folder + "basicTest_Environment9.csv", index_col=0)

    # Font for Plot
    font = {'family': 'serif', 'color':  'black', 'weight': 'normal', 'size': 16}
    fig, axes = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:2]:
        df[column].plot(ax=axes, x=df.columns[0])

    axes.set_title("Number of divisions - Trial 1", fontsize = 18)
    axes.set_xlabel("Time", fontsize=14)
    axes.legend(["Number of divisions (Food: 0, Refill: 1000)"], loc='upper center', bbox_to_anchor=(0.5, -0.16),
          fancybox=True, shadow=True, ncol=5)

    plt.show

save_basicTest_Environment9("DataCollection/")
retrieve_basicTest_Environment9("DataCollection/")
retrieve_basicTest_Environment9__t1("DataCollection/")
