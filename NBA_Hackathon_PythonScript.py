# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:30:42 2019

@author: Peter Law, Xingyuan Gu
"""

#imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.model_selection import cross_val_score
import numpy as np

#import training dataset
train_df = pd.read_csv(r'D:\NBABusComp\5_full_Modified.csv')

#see the columns names in the data
train_df.info()

#checking a few lines of the dataset
train_df.head()

#X,Y Dataset Creation
Y_data = train_df['Engagements']
X_data = train_df.drop('Engagements', axis=1)

#Split into training and test set for modeling
X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size=0.3, random_state=200)

#Training the model
lm = LinearRegression()
lm.fit(X_train, Y_train)

#Check Scores for Data Sets
lm.score(X_test, Y_test)
lm.score(X_train, Y_train)

#Checking Yhat for Train and Test Data
yhat_train = lm.predict(X_train)
yhat_train[0:5]

yhat_test = lm.predict(X_test)
yhat_test[0:5]

#Visualizing Training Data Set
plt.figure()

ax1 = sns.distplot(Y_train, hist=False, color="r", label="Actual Value (Train)")
sns.distplot(yhat_train, hist=False, color="b", label="Predicted Values (Train)" , ax=ax1)

plt.title('Actual Training Data vs Fitted Training Data for Engagement')
plt.xlabel('Engagement_Level')
plt.ylabel('Types')

plt.show()
plt.close()

#Visualizing Testing Data Set
plt.figure()

ax1 = sns.distplot(Y_test, hist=False, color="r", label="Actual Value (Test)")
sns.distplot(yhat_test, hist=False, color="b", label="Predicted Values (Test)" , ax=ax1)

plt.title('Actual Testing Data vs Fitted Testing Data for Engagement')
plt.xlabel('Engagement_Level')
plt.ylabel('Types')

plt.show()
plt.close()

#Cross Validation 
Rcross = cross_val_score(lm, X_data, Y_data, cv=4)
Rcross

#Parameters
lm.intercept_
lm.coef_

#Compare Predicted values with Actual values (with output)
Y_test2 = np.array(Y_test)
name = ['Actual_Test']
test=pd.DataFrame(columns=name,data=Y_test2)
test.to_csv('D:/NBABusComp/Results_Actual.csv', encoding='utf-8')

yhat_test2 = np.array(yhat_test)
name = ['Prediction_Test']
test=pd.DataFrame(columns=name,data=yhat_test2)
test.to_csv('D:/NBABusComp/Results_Prediction.csv', encoding='utf-8')

################################
#Model creation for Holdout_set#
################################

#Import Holdout Set
train_df1 = pd.read_csv(r'D:\NBABusComp\holdout_set_draft.csv')

#X,Y Dataset Creation (holdout set)
Y_data = train_df['Engagements']
X_data = train_df.drop('Engagements', axis=1)
Y_Holdout = train_df1['Engagements']
X_Holdout = train_df1.drop('Engagements',axis=1)

lm1 = LinearRegression()
lm1.fit(X_data, Y_data)

#Checking Yhat for Training and Holdout Data
yhat_train1 = lm1.predict(X_data)
yhat_train1[0:5]

yhat_test1 = lm1.predict(X_Holdout)
yhat_test1[0:5]

#Parameters
lm1.intercept_
lm1.coef_

#Storing Holdout_set predictions
yhat_test1 = np.array(yhat_test1)
name = ['Prediction_Test']
test1=pd.DataFrame(columns=name,data=yhat_test1)
test1.to_csv('D:/NBABusComp/Holdout_Results_Prediction.csv', encoding='utf-8')

#Visualizing Holdout Data Set (Predicted) vs Actual Engagement from Training Data
plt.figure()

ax1 = sns.distplot(Y_data, hist=False, color="r", label="Actual Value (Test)")
sns.distplot(yhat_test1, hist=False, color="b", label="Predicted Values (Test)" , ax=ax1)

plt.title('Actual Testing Data vs Fitted Testing Data for Engagement')
plt.xlabel('Engagement_Level')
plt.ylabel('Types')

plt.show()
plt.close()