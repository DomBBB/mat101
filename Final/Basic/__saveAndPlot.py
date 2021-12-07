# STORE
df = pd.DataFrame(columns=["cycle", "population", "no_active", "no_passive", "uptake_active", "uptake_passive", "metabolite_active", "metabolite_passive"], index=list(range(len(res))))

for idx, item in enumerate(res):
    df.loc[idx] = pd.Series({"cycle": item[0],
    "population": item[1],
    "no_active": item[2],
    "no_passive": item[3],
    "uptake_active": item[4]["up_active"],
    "uptake_passive": item[4]["up_passive"],
    "metabolite_active": item[4]["me_active"],
    "metabolite_passive": item[4]["me_passive"]})

df = df.set_index(["cycle"])
df.to_csv("geneticExchange")


# RETRIEVE
df = pd.read_csv("geneticExchange", index_col=0)

for column in df.columns[:3]:
    df[column].plot(label = column)
plt.legend()
plt.show

for column in df.columns[3:]:
    df[column].plot()
plt.legend()
plt.show



def retrieve_basicTest_variableSize(file_folder):
    df = pd.read_csv(file_folder + "_basicTest_variableSize", index_col=0)

    fig, axes = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

    for column in df.columns[1:3]:
        df[column].plot(ax=axes[0], x=df.columns[0], label=column)
    for column in df.columns[4:6]:
        df[column].plot(ax=axes[1], x=df.columns[3], label=column)
    for column in df.columns[7:9]:
        df[column].plot(ax=axes[2], x=df.columns[6], label=column)

    axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, -0.3),
          fancybox=True, shadow=True, ncol=5)
    plt.show
