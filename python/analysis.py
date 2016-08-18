import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

data = pd.read_csv("../data/pbp-2015.csv")

data.head()

data.columns

data["Formation"].unique()

offensive_formation_filter = lambda x: x["Formation"] not in [np.nan, "FIELD GOAL", "PUNT"]
offensive_formations = data.loc[data.apply(offensive_formation_filter, axis=1),:]

offensive_formations["Formation"].unique()


offensive_formations.groupby(["Formation"]).size().plot(kind="bar")
plt.savefig("../img/formation_distribution.png", bbox_inches="tight")
