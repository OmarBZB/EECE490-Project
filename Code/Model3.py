import pandas as pd

def recommend3(userid):
    df = pd.read_csv('RecipeRatingsTransformed.csv')
    userCol = df.user.ne(userid).idxmin()
    if(userCol==0 and userid != 1):
        return
    num=0
    highRatedRecipes = []
    while (df.iloc[userCol,0] == userid):
        if (df.iloc[userCol,2] == 5 or df.iloc[userCol,2] == 4):
            highRatedRecipes.append((df.iloc[userCol,1],df.iloc[userCol,2],df.iloc[userCol,3]))
        userCol+=1
        num+=1
        if (len(df)==userCol):
            break
    ratings = pd.DataFrame(df.groupby('names')['rating'].mean())
    ratings['num of ratings'] = pd.DataFrame(df.groupby('names')['rating'].count())
    df2 = df.pivot_table(index='user',columns='names',values='rating')
    corrList = []
    for i in range(len(highRatedRecipes)):
        recipeRatings = df2[highRatedRecipes[i][2]]
        recipeSimilar = df2.corrwith(recipeRatings)
        corrRecipe = pd.DataFrame(recipeSimilar,columns=['Correlation'])
        corrRecipe.dropna(inplace=True)
        corrList.append((corrRecipe,highRatedRecipes[i][0]))

    
    df3 = pd.read_csv('RecipeNames.csv')
    df3 = df3.sort_values('name')
    avgCorrList = []
    for i in range(len(corrList[0][0])):
        orderj = []
        sum = 0
        for j in range(len(corrList)):
            sum+=corrList[j][0].Correlation[i]
            orderj.append((corrList[j][0].Correlation[i],corrList[j][1]))
        orderj.sort(key=lambda tup: tup[0], reverse=True)        
        avgCorrList.append((df3.iloc[i,1],df3.iloc[i,0],sum/len(corrList),orderj))
    MaxCorrList = []
    for i in range(len(corrList[0][0])):
        orderj = []
        max = -2
        for j in range(len(corrList)):
            if(corrList[j][0].Correlation[i]>max):
                max=corrList[j][0].Correlation[i]
            orderj.append((corrList[j][0].Correlation[i],corrList[j][1]))
        orderj.sort(key=lambda tup: tup[0], reverse=True)        
        MaxCorrList.append((df3.iloc[i,1],df3.iloc[i,0],max,orderj))
        
    temp=[]
    userCol = df.user.ne(userid).idxmin()
    
    while (df.iloc[userCol,0] == userid):
        temp.append(df.iloc[userCol,1])
        userCol+=1
        if (len(df)==userCol):
            break
        
    for i in temp:
        for tup in avgCorrList:
            if (i == tup[1] or tup[1]==32 or tup[1]==31 or tup[1]==5):
                avgCorrList.remove(tup)
    for i in temp:
        for tup in MaxCorrList:
            if (i == tup[1]):
                MaxCorrList.remove(tup)
    for i in range(len(MaxCorrList)):
        if(MaxCorrList[i][2]>0.7):
            print("in max",i)
            avgCorrList[i]=MaxCorrList[i]
    avgCorrList.sort(key=lambda tup: tup[2], reverse=True)
    print("Model 3 recommends the following to user",userid,":")
    toreturn = []
    i=0
    while (len(toreturn)<5 and len(avgCorrList)>0):
        
        if(avgCorrList[i][1]==32 or avgCorrList[i][1]==31 or avgCorrList[i][1]==5):
            i+=1
        else:
            if(len(highRatedRecipes)>10):
                toreturn.append((avgCorrList[i][0],avgCorrList[i][3][0][1],avgCorrList[i][3][1][1],avgCorrList[i][3][2][1]))
            elif(len(highRatedRecipes)>5):
                toreturn.append((avgCorrList[i][0],avgCorrList[i][3][0][1],avgCorrList[i][3][1][1]))
            else:
                toreturn.append((avgCorrList[i][0],avgCorrList[i][3][0][1]))
            i+=1
        if (len(avgCorrList)==i):
            break
    df3 = df3.sort_values('item')
    
    if(len(highRatedRecipes)>20):
        for i in range(len(toreturn)):
            print("we recommend :",toreturn[i][0],"because you liked :",df3.iloc[toreturn[i][1]-1,1],"and",df3.iloc[toreturn[i][2]-1,1],"and",df3.iloc[toreturn[i][3]-1,1])
    elif(len(highRatedRecipes)>8):
        for i in range(len(toreturn)):
            print("we recommend :",toreturn[i][0],"because you liked :",df3.iloc[toreturn[i][1]-1,1],"and",df3.iloc[toreturn[i][2]-1,1])
    else:
        for i in range(len(toreturn)):
            print("we recommend :",toreturn[i][0],"because you liked :",df3.iloc[toreturn[i][1]-1,1])
