import random
import pandas as pd
from Model1 import *
from Model2 import *
from Model3 import *
from Model4 import *
from GenerateMatrix import *
import csv

df = pd.read_csv("RecipeRatingsTransformed.csv")
df2 = pd.read_csv("RecipeNames.csv")
df3 = pd.read_csv("Usernames.csv")

con = None
while con is None:
    try:
        con = int(input("\nPlease enter '1' to sign up or '0' to sign in: "))
    except:
         pass

if (con == 1):
    a = str(input("\nPlease enter a username (Don't forget it!): "))
    userid = df.iloc[len(df)-1,0] + 1
    with open('Usernames.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        data = [userid,a]
        writer.writerow(data)
    
    count = 0
    while (count < 5 or count > 40):
        try:
            count = int(input("\nHow many dishes are you willing to rate (5-40): "))
        except:
            pass
    indices = random.sample(range(0,63),count)
    listRatings = []
    for i in range(count):
        recipeID = df2.iloc[indices[i],0]
        recipe = df2.iloc[indices[i],1]
        rating = 0
        while (rating < 1 or rating > 5):
            try:
                rating = int(input("\nPlease rate the following recipe '"+recipe+"' from 1 - 5: "))
            except:
                pass
        listRatings.append((recipeID,rating,recipe))
    matrix_factorization(500,0.001,0.01) 
    with open('RecipeRatingsTransformed.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for i in range(len(listRatings)):
            data = [userid,listRatings[i][0],listRatings[i][1],listRatings[i][2]]
            writer.writerow(data)
    with open('RecipeRatings.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        data = [0]*63
        data[0] = "2021/12/04 12:27:53 AM GMT+2"
        for i in range(1,63):
            for j in range(len(listRatings)):
                if(i==listRatings[j][0]):
                    data[i]=listRatings[j][1]
        writer.writerow(data)
            
    recommend1(userid)
    recommend2(userid)
    recommend3(userid)
    recommend4(userid)
    
    
    
                

elif (con == 0):
    a = str(input("\nPlease enter your username: "))
    userid = 0
    for i in range(len(df3)):
        if(a==df3.username[i]):
            userid = df3.user_id[i]
            break
    recommend1(userid)
    recommend2(userid)
    recommend3(userid)
    recommend4(userid)
    
    
    
       