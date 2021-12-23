import pandas as pd
import random
from surprise import Dataset
from surprise import Reader
from surprise import KNNWithMeans
from surprise.model_selection import GridSearchCV


df = pd.read_csv("RecipeRatingsTransformed.csv")
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[["user", "item", "rating"]], reader)
sim_options = {
    "name": "msd",
    "min_support": 3,
    "user_based": False,
}

param_grid = {"sim_options": sim_options}

trainingSet = data.build_full_trainset()
algo = KNNWithMeans(sim_options=sim_options)
algo.fit(trainingSet)

prediction = algo.predict(1, 0)

list = []
#userid = random.randint(0, 251)
userid = 270
print(userid)

for i in range(64):
        prediction = algo.predict(userid, i+1)
        list.append((prediction.est,i,df.iloc[i,3]))

userCol = df.user.ne(userid).idxmin()
a = 0
while (df.iloc[userCol,0] == userid):
    del list[df.iloc[userCol,1]-a]
    userCol+=1
    if(userCol==len(df)):
        break
    a+=1
list.sort(key=lambda tup: tup[0], reverse=True)
print(list)