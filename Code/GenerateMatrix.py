#!/usr/bin/env python3
import pandas as pd
import numpy as np
import csv
df = pd.read_csv("RecipeRatings.csv")
df2 = pd.read_csv("RecipeNames.csv")
			
def matrix_factorization(steps=500, alpha=0.001, beta=0.01):
	nUsers=len(df)
	num_features=3
	R = [ [ 0 for i in range(64) ] for j in range(nUsers) ]
	for i in range(nUsers-1):
		for j in range(63):
			if(df.iloc[i,j]==1 or df.iloc[i,j]==2 or df.iloc[i,j]==3 or df.iloc[i,j]==4 or df.iloc[i,j]==5):
				R[i][j] = df.iloc[i+1][j+1]
			else:
				R[i][j] = 0
	teta= np.random.rand(nUsers,num_features)
	X = np.random.rand(63,num_features)
	
	X = X.T
	for step in range (steps):
		for i in range (len (R)):
			for j in range (len (R[i])):
				if R[i][j] > 0:
					eij = R[i][j]-np.dot (teta[i,:],X[:,j])
				
					for k in range (num_features):
						teta[i][k] = teta[i][k] + alpha * (eij * X[k][j] - beta * teta[i][k])
						X[k][j] = X[k][j] + alpha * (eij * teta[i][k] - beta * X[k][j])
		eR = np.dot(teta,X)
		
		e = 0
		
		for i in range (len(R)):
			for j in range (len(R[i])):
				if R[i][j] > 0:
					e = e + pow(R[i][j]-np.dot(teta[i,:],X[:,j]), 2)
		
		if e < 0.001:
			break
	Matrix = np.dot(teta, X)
	header = []
	for i in range (len(df2)):
		header.append(df2.iloc[i,1])
	with open('Matrix.csv', 'w', encoding='UTF8', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(header)
		for i in range(len(Matrix)):
			data = Matrix[i]
			writer.writerow(data)
		
