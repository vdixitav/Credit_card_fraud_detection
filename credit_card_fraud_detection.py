# -*- coding: utf-8 -*-
"""Credit card fraud detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZAy9c_PCzMKh7r2jeDWhbap3KJXggwYk
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# loading dataset to pandas dataframe

credit_card_data=pd.read_csv("/content/creditcard.csv",delimiter=',', on_bad_lines='skip') # skip lines that cause errors

credit_card_data.head()

credit_card_data.tail()

credit_card_data.info()

# missing values check
credit_card_data.isnull().sum()

credit_card_data.isnull().sum().sum()

credit_card_data['Class'].value_counts()

# filling missing values
credit_card_data.fillna(credit_card_data.mean(), inplace=True)

credit_card_data.isnull().sum()

# distribution of legit tranctn and fraudulent tranctn

credit_card_data['Class'].value_counts()

credit_card_data['Class']=credit_card_data['Class'].replace(0.004581,0.000000 )

credit_card_data['Class'].value_counts()

# dataset is hightly imbalance
legit=credit_card_data[credit_card_data.Class==0]
fraud=credit_card_data[credit_card_data.Class==1]

print(legit.shape)
print(fraud.shape)

#statistical mearures of data

legit.Amount.describe()

fraud.Amount.describe()

# COMPARE THE VLAUES FOR BOTH TRANCTN

credit_card_data.groupby('Class').mean()

# dealing with unbalance data
# under-sampling-build a sample dataset from orginal containing similar distribution of normal transaction

legit_sample=legit.sample(n=492)

from types import new_class
# concatinating two dataframe

new_class=pd.concat([legit_sample,fraud],axis=0)# row

new_class.head()

new_class.tail()

new_class['Class'].value_counts()

new_class.groupby('Class').mean()

# spliting data into features and target

X=new_class.drop(columns='Class',axis=1)
Y=new_class['Class']

print(X)

print(Y)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

# model training

model=LogisticRegression()

# training the model
model.fit(X_train,Y_train)

# accuracy score on training data
X_train_prediction=model.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)

print('Accuracy on training data:',training_data_accuracy)

# accuracy on test data
X_test_prediction=model.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,Y_test)

print('Accuracy on test data:',test_data_accuracy)
