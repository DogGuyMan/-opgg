import pandas as pd

raw_DF = pd.read_csv("SubPlayer.csv", sep=",")
raw_DF["winRatio"] = round(raw_DF["winRatio"], 4)
platform = ["eun1", "euw1", "jp1", "kr", "la1", "la2", "ru"]
for i in platform:
    temp = raw_DF[raw_DF["region"] == i]
    temp.to_csv(f'Sub_{i}.csv', index=False, header=True, na_rep='-')
