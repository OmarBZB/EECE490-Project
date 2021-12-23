#!/usr/bin/env python3
import pandas as pd
import random
import csv

df = pd.read_csv("RecipeRatings.csv")

header1 = ['user', 'item', 'rating','names']

with open('RecipeRatingsTransformed.csv', 'w', encoding='UTF8',  newline='') as f:
	writer = csv.writer(f)
	
	# write the header
	writer.writerow(header1)
	for i in range(1,len(df)):
		for j in range(1,64):
			#write the data
			if(df.iloc[i,j]==1 or df.iloc[i,j]==2 or df.iloc[i,j]==3 or df.iloc[i,j]==4 or df.iloc[i,j]==5):
				x=0
				if(x==0):
					data = [i,j,df.iloc[i,j],df.columns[j]]
					writer.writerow(data)
					
header2 = ['item', 'name']

with open('RecipeNames.csv', 'w', encoding='UTF8', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(header2)
	for i in range(1,64):
		data = [i,df.columns[i]]
		writer.writerow(data)



		