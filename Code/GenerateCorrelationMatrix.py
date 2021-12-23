#!/usr/bin/env python3

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 4
df = pd.read_csv('RecipeRatings.csv')
corrMatrix = df.corr()
sn.heatmap(corrMatrix, cmap="Reds")
plt.show()