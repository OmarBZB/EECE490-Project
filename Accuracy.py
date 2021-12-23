#!/usr/bin/env python3
from surprise import Dataset
from surprise import Reader
from surprise import KNNWithMeans

from Model1 import * 
from Model2 import * 

real = pd.read_csv("RecipeRatings.csv")
realtransformed = pd.read_csv("RecipeRatingsTransformed.csv")
predictedMatrix = real = pd.read_csv("Matrix.csv")

def measureError():
	error1 = 0
	error2 = 0
	error3 = 0
	
	reader1 = Reader(rating_scale=(1, 5))
	data1 = Dataset.load_from_df(realtransformed[["user", "item", "rating"]], reader1)
	sim_options1 = {
		"name": "msd",
		"min_support": 3,
		"user_based": False,
	}
	
	param_grid1 = {"sim_options": sim_options1}
	
	trainingSet1 = data1.build_full_trainset()
	algo1 = KNNWithMeans(sim_options=sim_options1)
	algo1.fit(trainingSet1)
	
	reader2 = Reader(rating_scale=(1, 5))
	data2 = Dataset.load_from_df(realtransformed[["user", "item", "rating"]], reader2)
	sim_options2 = {
		"name": "cosine",
		"min_support": 3,
		"user_based": True,
	}
	
	param_grid2 = {"sim_options": sim_options2}
	
	trainingSet2 = data2.build_full_trainset()
	algo2 = KNNWithMeans(sim_options=sim_options2)
	algo2.fit(trainingSet2)
	
	for i in range(len(realtransformed)):
		error1+=(realtransformed.iloc[i,2]-algo1.predict(realtransformed.iloc[i,0], realtransformed.iloc[i,2]).est)**2
		error2+=(realtransformed.iloc[i,2]-algo2.predict(realtransformed.iloc[i,0], realtransformed.iloc[i,2]).est)**2
		
	
	for i in range(len(predictedMatrix)):
		for j in range(62):
			if(real.iloc[i,j+1]>0):
				error3+=(predictedMatrix.iloc[i,j]-real.iloc[i,j+1])**2
	print("Error Model 1 is :",error1/len(realtransformed))
	print("Error Model 2 is :",error2/len(realtransformed))
	print("Error Model 4 is :",error3/len(realtransformed))
	
	
measureError()
	
	