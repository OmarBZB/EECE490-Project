import pandas as pd

def recommend4(userid):
	df = pd.read_csv("Matrix.csv")
	list = df.iloc[userid-1]
	list1 = []
	df2 = pd.read_csv("RecipeNames.csv")
	for i in range(len(list)):
		list1.append((list[i],df2.iloc[i,0],df2.iloc[i,1]))
	list1.sort(key=lambda tup: tup[0], reverse=True)
	
	print("Model 4 recommends the following:")
	
	toreturn = []
	i=0
	while (len(toreturn)<5):
		if(list1[i][1]==32 or list1[i][1]==31 or list1[i][1]==5):
			i+=1
		else:
			toreturn.append(list1[i][2])
			i+=1
	print(toreturn)
	
	