import utils
import pandas as pd
import numpy as np
# import scikit learn databases
from sklearn import datasets
from sklearn.model_selection import train_test_split
from datetime import datetime



frame=pd.read_table('../resources/data.csv',skiprows=3, header=None,usecols=range(0,4), delimiter=',')
frame.columns=["Date","Time","total","daily"]
# define the columns names of the data then convert to dataframe

df = frame
# print the df and shape to get a better understanding of the data
print(df.shape)
print(df)

data=df.to_numpy()
print(data)


X_train, X_test, y_train, y_test = train_test_split(df, data, test_size = 0.25)
# validate set shapes
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

from timeit import default_timer as timer
start_ho = timer()
# fit a model using linear model method from sklearn
from sklearn import linear_model

lm = linear_model.LinearRegression()
model = lm.fit(X_train, y_train)
# generate predictions
predictions = lm.predict(X_test)
end_ho = timer()
# calcualte function runtime
time_ho = (end_ho - start_ho)
# show predictions
print(predictions)
https://stackoverflow.com/questions/16453644/regression-with-date-variable-using-scikit-learnàcv