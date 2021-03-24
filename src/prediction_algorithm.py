import utils
import pandas as pd
import numpy as np
# import scikit learn databases
from sklearn import datasets
from sklearn.model_selection import train_test_split
from datetime import datetime



frame=pd.read_table('resources\data.csv',skiprows=3, header=None,usecols=range(0,4), delimiter=',')
frame.columns=["Date","Time","total","daily"]
# define the columns names of the data then convert to dataframe

df = frame
# print the df and shape to get a better understanding of the data
print(df.shape)
print(df)

data=df.to_numpy()
print(data)

