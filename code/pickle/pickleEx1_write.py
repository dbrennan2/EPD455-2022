import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets
import pandas as pd
import pickle

# load the inbuit diabetes dataset
diabetes = datasets.load_diabetes()
# print(diabetes.DESCR)


# create a database of the data
db_df = pd.DataFrame(diabetes.data,columns=diabetes.feature_names)


# add a column in that database called progression - this is what we are predicting
db_df['Progression'] = diabetes.target


# feautures
x = db_df.drop(labels='Progression', axis=1) 
# target - what we predict
y = db_df['Progression']

# split the data into training and test sets
train_x, test_x, train_y, test_y = train_test_split(x,y,test_size=0.25,random_state=999)
print(train_x.shape)
print(test_x.shape)
print(train_y.shape)
print(test_y.shape)

# define a linear regressor
lm = LinearRegression()

# fit the linear regressor model
lm.fit(train_x, train_y)

# dump the model into a pickle file for later use
filename = 'lm_model1.pkl'
pickle.dump(lm, open(filename, 'wb'))

# dump the test x
filename = 'testx.pkl'
pickle.dump(test_x, open(filename, 'wb'))

# dump the test y
filename = 'testy.pkl'
pickle.dump(test_y, open(filename, 'wb'))