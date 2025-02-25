import paho.mqtt.client as mqtt
import time
import requests
import test
import subprocess

class broker_subpub():
    def _init_(self):
        self.gender = None
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.client.connect("test.mosquitto.org", 1883, 60)
        self.client.loop_start()
        self._loop()
    def on_connect(self, client, userdata, flags, rc):
        print("Connected to server (i.e., broker) with result code "+str(rc))
        self.client.subscribe("paho/gender")
    def on_message(self, client, userdata, msg):
        msg = str(msg.payload, "utf-8")
        print("received: " + msg)
        if self.gender == "male":
            print("male")
        elif self.gender == "female":
            print("female")
        else:
            return
    def _loop(self, ):
        while True:
                time.sleep(1)
                subprocess.check_output("sh test.sh", shell=1)
                self.gender = test.get_gender("test-mic.wav")
                self.client.publish("paho/gender", self.gender)
                time.sleep(20)
if __name__ == '__main__':
    sps = broker_subpub()._init_()
