import pickle
import pandas as pd
import numpy
import paho.mqtt.client as mqtt

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
        return int(elem)
    
infile = open('finalized_model_long.pkl','rb')
new_dict = pickle.load(infile)
classifier=new_dict[0]

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

#x=attention,meditation,delta,theta,lowAplha,highAlpha,lowBeta,highBeta,lowGamma,highGamma
#print(x)
    
def on_message(client, userdata, msg):    
    x = str(msg.payload)[2:-1].split(",")
    for i in range(len(classifier)):
        if isinstance(classifier[i], int):
            classifier[i]=x[classifier[i]]
    ww=evaluatestack(classifier)
                
    if(ww > 0.9):
        print('3')
    elif(ww > 0.5 and ww < 0.8):
        print('2')
    elif(ww > 0.8 and ww < 0.9):
        print('1')
    else:
        print('0')

    x.clear()

client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker_ip, 1883)
client.loop_forever()
client.disconnect()
