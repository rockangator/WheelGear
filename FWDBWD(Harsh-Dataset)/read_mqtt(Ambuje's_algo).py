# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:14:55 2019

@author: ambuj
"""
from keras.models import model_from_json
import json
import numpy as np
import paho.mqtt.client as mqtt
#Location Of JSON file
json_file = open('C:\\Users\\ambuj\\Desktop\\fwdbwd.json', 'r')

loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
# Write the file name of the weights
loaded_model.load_weights("C:\\Users\\ambuj\\Desktop\\fwdbwd_weights.h5")
print("Loaded model from disk")



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
    x = str(msg.payload)[2:-1].split(",")
    #x=attention,meditation,delta,theta,lowAplha,highAlpha,lowBeta,highBeta,lowGamma,highGamma
    y=np.array(x,'float64')

    l=[]
    for i in range(0,len(y)):
        a=max(y)
        l.append(a)
        for j in range(0,len(y)):
            y[i]=y[i]/a
            
    
        
    for j in range(0,len(y)):
        c=0
        a=format(y[i], '.65f')
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
            y[i]=float(a)*sss
        elif c==3:
            y[i]=float(a)*10
    y=y.reshape(1,8)
    prediction = loaded_model.predict(y)
    if prediction[0][0] >0.5:
        print("Forword")
    else:
        print("Backword")
    

client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker_ip, 1883)
client.loop_forever()
client.disconnect()
