import paho.mqtt.client as mqtt

import time
import RPi.GPIO as gpio

def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(27, gpio.OUT)
 gpio.setup(22, gpio.OUT)
 gpio.setup(23, gpio.OUT)
 gpio.setup(24, gpio.OUT)
 
def forward(sec):
 init()
 gpio.output(27, True) #Motor1 -
 gpio.output(22, False)#Motor1 +
 gpio.output(23, False)#Motor2 +
 gpio.output(24, True) #Motor2 -
 time.sleep(sec)
 gpio.cleanup()
 
def reverse(sec):
 init()
 gpio.output(27, False)
 gpio.output(22, True)
 gpio.output(23, True)
 gpio.output(24, False)
 time.sleep(sec)
 gpio.cleanup()

def stop(sec):
 init()
 gpio.output(27, False)
 gpio.output(22, False)
 gpio.output(23, False) 
 gpio.output(24, False)
 time.sleep(sec)
 gpio.cleanup()
 
def right(sec):
 init()
 gpio.output(27, True)
 gpio.output(22, False)
 gpio.output(23, False) 
 gpio.output(24, False)
 time.sleep(sec)
 gpio.cleanup()
 
def left(sec):
 init()
 gpio.output(27, False)
 gpio.output(22, False)
 gpio.output(23, False) 
 gpio.output(24, True)
 time.sleep(sec)
 gpio.cleanup()
 
mqtt_username = "username"
mqtt_password = "qwertyuiop"
#mqtt_topic = "test1"
mqtt_topic = "runbot"
mqtt_broker_ip = "192.168.43.131"

client = mqtt.Client()
client.username_pw_set(mqtt_username, mqtt_password)
def on_connect(client, userdata, flags, rc):
    print ("Connected!", str(rc))
    client.subscribe(mqtt_topic)
    
def on_message(client, userdata, msg):    
    x = str(msg.payload)[2]
    print(x)
    if x == 'F':
        forward(1)
    if x == 'B':
        backward(1)
    if x == 'L':
        left(1)
    if x == 'R':
        right(1)
    

client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker_ip, 1883)
client.loop_forever()
client.disconnect()

