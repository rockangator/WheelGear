# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:18:34 2019

@author: ambuj
"""


import numpy as np

import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Dense

from keras.layers import Dropout , Flatten

from sklearn import preprocessing
#Give the pathof the file
data=pd.read_csv('harshbwdfwd.csv',encoding='utf-8')
#data=pd.read_csv('training',delimiter='\t',encoding='utf-8')
x_data=data.iloc[:,0:10]
y_data=data.iloc[:, -1]
y=np.array(x_data,'float64')
#Pre-Processing of data

#Splitting into train-test
X_train, X_test, Y_train, Y_test = train_test_split(x_data, y_data, test_size=0.20)
print('x_train shape:',X_train.shape)
print('x_test shape:', X_test.shape)
print('Y_train shape:', Y_train.shape)
print('Y_test shape:', Y_test.shape)

model_classifier_ann = Sequential()

# Adding the input layer and the first hidden layer
model_classifier_ann.add(Dense(units = 60, kernel_initializer = 'uniform', activation = 'relu', input_dim=10))
model_classifier_ann.add(Dropout(0.2))

# Adding the second hidden layer
model_classifier_ann.add(Dense(units = 60, kernel_initializer = 'uniform', activation = 'relu'))
model_classifier_ann.add(Dropout(0.2))
model_classifier_ann.add(Dense(units = 60, kernel_initializer = 'uniform', activation = 'relu'))
model_classifier_ann.add(Dropout(0.2))
model_classifier_ann.add(Dense(units = 60, kernel_initializer = 'uniform', activation = 'relu'))
model_classifier_ann.add(Dropout(0.2))

model_classifier_ann.add(Dense(units = 60, kernel_initializer = 'uniform', activation = 'relu'))
model_classifier_ann.add(Dropout(0.2))



# Adding the output layer
model_classifier_ann.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
model_classifier_ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
model_classifier_ann.summary()

# Fitting the ANN to the Training set
model_classifier_ann.fit(X_train, Y_train, batch_size = 64, epochs =500,validation_data=(X_test, Y_test))


score, acc = model_classifier_ann.evaluate(X_test, Y_test, batch_size=32)
print('Test score:', score)
print('Test accuracy:', acc)


# serialize model to JSON
model_json = model_classifier_ann.to_json()

# Write the file name of the model

with open("pkmkb.json", "w") as json_file:
    json_file.write(model_json)
    
# serialize weights to HDF5
# Write the file name of the weights
model_classifier_ann.save_weights("pkmkb_weights.h5")
print("Saved model to disk")

    
    
