import paho.mqtt.client as mqtt
import time
import matplotlib.pyplot as plt
#from pyAudioAnalysis import audioTrainTest as aT
import requests

#from model import model

class broker_subpub():
    def _init_(self):
        self.gender = None
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.client.connect("eclipse.usc.edu", 11000, 60)
        self.client.loop_start()
        #self.model = Model()
        self._loop()
    def on_connect(self, client, userdata, flags, rc):
        print("Connected to server (i.e., broker) with result code "+str(rc))
        self.client.subscribe("paho/gender")
    def on_message(self, client, userdata, msg):
        msg = str(msg.payload, "utf-8")
        print("received: " + msg.topic)
        if self.gender == "male":
            print("male")
        elif self.gender == "female":
            print("female")
        else:
            return
    def _loop(self, ):
        while True:
                time.sleep(1)
                self.client.publish("paho/gender", self.gender)
if __name__ == '__main__':
    sps = broker_subpub()
