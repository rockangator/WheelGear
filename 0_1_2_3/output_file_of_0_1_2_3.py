# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:51:31 2019

@author: ambuj
"""

import pickle
import pandas as pd
import numpy

def sig(x):
    
    if x>51:
        return 1
    else:
        return 1/(1+numpy.exp(-x))

def evaluatestack(stack):
    elem = stack.pop(0)

    if (elem == '-'):
        return evaluatestack(stack) - evaluatestack(stack)
    elif (elem == '+'):
        return evaluatestack(stack) + evaluatestack(stack)
    elif (elem == '/'):
        try:
            return evaluatestack(stack) / evaluatestack(stack)
        except:
            return 0
    elif (elem == '*'):
        return evaluatestack(stack) * evaluatestack(stack)
    elif(elem=='P'):
         return sig(evaluatestack(stack)+evaluatestack(stack))
    elif(elem=="W"):
        return evaluatestack(stack)*evaluatestack(stack)
    else:
        # print(type(elem))
        return int(elem)
    
infile = open('0_1_2_3_classifier.pkl','rb')
new_dict = pickle.load(infile)
infile.close()
b=[61,51,3383,16655,85853,23204,12102,6185,5644,1392]
classifier=new_dict[0]
for i in range(20):
    
    if isinstance(classifier[i], int):
        classifier[i]=b[classifier[i]]
a=(evaluatestack(classifier))

            
if(a > 0.9):
    print('3')
elif(a > 0.5 and a< 0.8):
    print('2')
elif(a > 0.8 and a < 0.9):
    print('1')
else:
    print('0')
