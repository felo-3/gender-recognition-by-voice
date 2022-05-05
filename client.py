#

# paho.mqtt.client - This code provides a client class which enable applications to connect to an MQTT broker
#                    to publish messages, and to subscribe to topics and receive published messages. It also provides
#                    some helper functions to make publishing one off messages to an MQTT server very straightforward.

# sys -              The sys module in Python provides various functions and variables that are used to manipulate 
#                    different parts of the Python runtime environment. It allows operating on the interpreter as it 
#                    provides access to the variables and functions that interact strongly with the interpreter.

# grovepi -          GrovePi is an open source platform for connecting Grove Sensors to the Raspberry Pi.

#

import paho.mqtt.client as mqtt
import time
import requests
import sys
from grovepi import *

#From GrovePi libraries
sys.path.append('../../Software/Python/')
import grovepi

led = 4

grovepi.pinMode(led,"OUTPUT")

class device_subpub():

    def __init__(self):
        self.update = False
        self.gender = None
        self.client = mqtt.Client()
        self.client.on_message = on_message
        self.client.on_connect = on_connect
        self.client.connect("test.mosquitto.org", 1883, 60)
    
    def on_connect(self, client, userdata, flags, rc):
        print("Connected to server (i.e., broker) with result code "+str(rc))
        self.client.subscribe("paho/gender")
        self.client.message_callback_add("paho/gender", custom_callback)

    def on_message(self, client, userdata, msg):
        self.gender = str(msg.payload, "utf-8")
        print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))
        self.update = True

    def custom_callback(self, client, userdata, message):
        print(str(msg.payload, "utf-8"))
        
        if(str(msg.payload, "utf-8") == "male"):
            grovepi.digitalWrite(LED,1)
        elif(str(msg.payload, "utf-8") == "female"):
            grovepi.digitalWrite(LED,0)

    def loop_forever(self):
        self.client.loop_forever()
            
if __name__ == '__main__':
    dps = device_subpub()
    dps.loop_forever()
                
