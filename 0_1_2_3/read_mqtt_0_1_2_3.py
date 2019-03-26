# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:49:07 2019

@author: ambuj
"""

from keras.models import model_from_json
import json
import numpy as np
import paho.mqtt.client as mqtt
import pickle
import pandas as pd
import numpy


mqtt_username = "username"
mqtt_password = "qwertyuiop"
#mqtt_topic = "test1"
mqtt_topic = "wheelgear"
mqtt_broker_ip = "192.168.43.217"

client = mqtt.Client()
client.username_pw_set(mqtt_username, mqtt_password)
def on_connect(client, userdata, flags, rc):
    print ("Connected!", str(rc))
    client.subscribe(mqtt_topic)
    
def on_message(client, userdata, msg):    
    x = str(msg.payload)[:-1].split(",")
    #x=attention,meditation,delta,theta,lowAplha,highAlpha,lowBeta,highBeta,lowGamma,highGamma
    def sig(xx):
    
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
    b=list(map(int,x))
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
        

client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker_ip, 1883)
client.loop_forever()
client.disconnect()