# -*- coding: utf-8 -*-
"""DIABETES.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bvWFE21Rm3aV7nvcFUcqpEgmSJTIxJpW
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

diabetes_dataset = pd.read_csv('/content/diabetes1.csv')

diabetes_dataset.head()

diabetes_dataset.shape

diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

"""0 --> Non-Diabetic

1 --> Diabetic
"""

diabetes_dataset.groupby('Outcome').mean()

A = diabetes_dataset.drop(columns = 'Outcome', axis=1)
B = diabetes_dataset['Outcome']

print(A)

print(B)

"""Data Standardization"""

scaler = StandardScaler()

scaler.fit(A)

standardized_data = scaler.transform(A)

print(standardized_data)

A = standardized_data
B = diabetes_dataset['Outcome']

print(A)
print(B)

"""Training Test Split"""

A_train, A_test, B_train, B_test = train_test_split(A,B, test_size = 0.2, stratify=B, random_state=2)

print(A.shape, A_train.shape, A_test.shape)

"""Training Model"""

classifier = svm.SVC(kernel='linear')

classifier.fit(A_train, B_train)

"""Evaluating Model

Accuracy Score
"""

A_train_prediction = classifier.predict(A_train)
training_data_accuracy = accuracy_score(A_train_prediction, B_train)

print('Accuracy score of the training data : ', training_data_accuracy)

A_test_prediction = classifier.predict(A_test)
test_data_accuracy = accuracy_score(A_test_prediction, B_test)

from google.colab import drive
drive.mount('/content/drive')

print('Accuracy score of the test data : ', test_data_accuracy)

"""Checking using input data"""

input_data = (2,197,70,45,543,30.5,0.158,53)

# changing input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshaping the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardizing the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The individual is NON-DIABETIC.')
else:
  print('The individual is DIABETIC.')