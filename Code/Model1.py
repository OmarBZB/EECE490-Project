import pandas as pd
import random
from surprise import Dataset
from surprise import Reader
from surprise import KNNWithMeans
from surprise.model_selection import GridSearchCV

def recommend1(n):
    df = pd.read_csv("RecipeRatingsTransformed.csv")
    df2 = pd.read_csv("RecipeNames.csv")
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
    
    list = []
    userid = n
    for i in range(63):
            prediction = algo.predict(userid, i+1)
            list.append((prediction.est,i+1,df2.iloc[i,1]))

    userCol = df.user.ne(userid).idxmin()
    temp=[]
    
    while (df.iloc[userCol,0] == userid):
        temp.append(df.iloc[userCol,1])
        userCol+=1
        if (len(df)==userCol):
            break
        
    for i in temp:
        for tup in list:
            if i in tup:
                list.remove(tup)
                
    list.sort(key=lambda tup: tup[0], reverse=True)
    print("Model 1 recommends the following:")
    toreturn = []
    i=0
    while (len(toreturn)<5):
        if(list[i][1]==32 or list[i][1]==31 or list[i][1]==5):
            i+=1
        else:
            toreturn.append(list[i][2])
            i+=1
    print(toreturn)
    
