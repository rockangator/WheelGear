# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:33:11 2019

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
data=pd.read_csv('fwdbwd.csv',encoding='utf-8')
#data=pd.read_csv('training',delimiter='\t',encoding='utf-8')
x_data=data.iloc[:,0:8]
y_data=data.iloc[:, -1]
y=np.array(x_data,'float64')
#Pre-Processing of data
l=[]
for i in range(0,len(y)):
    a=max(y[i])
    l.append(a)
    for j in range(0,len(y[i])):
        y[i][j]=y[i][j]/a
        
for i in range(0,len(y)):
    
    for j in range(0,len(y[i])):
        c=0
        a=format(y[i][j], '.65f')
        for e in range(2,len(a)):
            if a[0]=='0' and a[1]=='.' :
                if a[e]!='0':
                    break
                c=c+1
               
        if c>3:
            w=c-2
            s="1"
            for r in range(0,w-1):
                s=s+s.join("0")
            sss=int(s)
            y[i][j]=float(a)*sss
        elif c==3:
            y[i][j]=float(a)*10

#Splitting into train-test
X_train, X_test, Y_train, Y_test = train_test_split(y, y_data, test_size=0.20)
print('x_train shape:',X_train.shape)
print('x_test shape:', X_test.shape)
print('Y_train shape:', Y_train.shape)
print('Y_test shape:', Y_test.shape)

#Artificial Neural Network Begins
model_classifier_ann = Sequential()

# Adding the input layer and the first hidden layer
model_classifier_ann.add(Dense(units = 60, kernel_initializer = 'uniform', activation = 'relu', input_dim=8))
model_classifier_ann.add(Dropout(0.2))

# Adding the second hidden layer
model_classifier_ann.add(Dense(units = 60, kernel_initializer = 'uniform', activation = 'relu'))
model_classifier_ann.add(Dropout(0.2))
model_classifier_ann.add(Dense(units = 60, kernel_initializer = 'uniform', activation = 'relu'))
model_classifier_ann.add(Dropout(0.2))
'''
model_classifier_ann.add(Dense(units = 60, kernel_initializer = 'uniform', activation = 'relu'))
model_classifier_ann.add(Dropout(0.2))
model_classifier_ann.add(Dense(units = 60, kernel_initializer = 'uniform', activation = 'relu'))
model_classifier_ann.add(Dropout(0.2))
model_classifier_ann.add(Dense(units = 60, kernel_initializer = 'uniform', activation = 'relu'))
model_classifier_ann.add(Dropout(0.2))'''




# Adding the output layer
model_classifier_ann.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
model_classifier_ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
model_classifier_ann.summary()

# Fitting the ANN to the Training set
model_classifier_ann.fit(X_train, Y_train, batch_size = 10, epochs =500,validation_data=(X_test, Y_test))


score, acc = model_classifier_ann.evaluate(X_test, Y_test, batch_size=10)
print('Test score:', score)
print('Test accuracy:', acc)

# serialize model to JSON
model_json = model_classifier_ann.to_json()

# Write the file name of the model

with open("fwdbwd.json", "w") as json_file:
    json_file.write(model_json)
    
# serialize weights to HDF5
# Write the file name of the weights
model_classifier_ann.save_weights("fwdbwd_weights.h5")
print("Saved model to disk")

    
    
