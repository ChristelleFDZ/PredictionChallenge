from download import download
from sklearn import linear_model, metrics
from sklearn.linear_model import LinearRegression
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt



url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv"
path_target = "resources\data.csv"
download(url, path_target, replace=True)

frame=pd.read_table("resources\data.csv",skiprows=3, header=None,usecols=range(0,4), delimiter=',')
frame.columns=["Date","Time","total","daily"]
# define the columns names of the data then convert to dataframe

df = frame

df= df[df["Time"].isnull() ==False]


def format_date(df):
    time_formated = pd.to_datetime(df['Date'] + " "+ df["Time"], format = '%d/%m/%Y %H:%M:%S')
    df['Date_formated']=time_formated
    return df

df = format_date(df)


#df1 = df1[df1['Time']<= '09:00:00']


df['Date']=pd.to_datetime(df['Date'])
df['Date']=df['Date'].map(dt.datetime.toordinal)


def timestr(tab1):
     d =[]
     cpt=0
     for item in tab1:
        time= datetime.strptime(item,'%H:%M:%S')
        int_time= time.hour*60+time.minute #we ignore the seconds
        d.insert(cpt,int_time)
       
        cpt+=1
     ser = pd.Series(np.array(d))
     return ser


df['Time']=timestr(df['Time'])
df= df[df["Time"].isnull() ==False]


#we use two explanatory variables
X=pd.DataFrame(np.c_[df['Time'],df['daily']],columns=['Time','daily'])
Y= df['Date']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.03, random_state=5)

#to create a axis for date and time:
#X_labels=pd.DataFrame(np.c_[df['Time'],df['daily']],columns=['Time','daily'])
#Y_labels= df['Date_formated']

#X_labels_train, X_labels_test, Y_labels_train, Y_labels_test = train_test_split(X_labels, Y_labels, test_size = 0.03, random_state=5)


lregression = LinearRegression()
lregression.fit(X_train, Y_train)

# Evaluation of training set
y_trainpredict = lregression.predict(X_train)
etype = (np.sqrt(mean_squared_error(Y_train, y_trainpredict)))
R2 = r2_score(Y_train, y_trainpredict)

 
# model evaluation for testing set
y_testpredict = lregression.predict(X_test)
etype = (np.sqrt(mean_squared_error(Y_test, y_testpredict)))
R2 = r2_score(Y_test, y_testpredict)


X_test=np.arange(0,len(X_test),1)

# Plot outputs
plt.scatter( X_test,Y_test,  color='black')
plt.plot( X_test,y_testpredict, color='red', linewidth=3)
#plt.yticks(Y_test,Y_labels_test) mathplolib hardly responsive
plt.show()

print('The result for the prediction is:')
print(np.sqrt(metrics.mean_squared_error(Y_test, y_testpredict)))

