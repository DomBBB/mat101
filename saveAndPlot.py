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
df

for column in df.columns[:3]:
    df[column].plot(label = column)
plt.legend()
plt.show

for column in df.columns[3:]:
    df[column].plot()
plt.legend()
plt.show


df.to_csv("geneticExchange")
