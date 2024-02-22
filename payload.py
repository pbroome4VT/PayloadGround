import time
from Telemetry import telemetry
from GEarth import gearth
import os

COM_PORT = "COM3"

count = 0
dataFile = None


UNKNOWN = -1
GPS = 1
IMU = 2
BAT = 3
def parse(msg):
    if(len(msg) >= 4):
        tag = msg[0:3]
        if(tag == "GPS"):
            return GPS
        elif(tag == "IMU"):
            return IMU
        elif(tag == "BAT"):
            return BAT
    return UNKNOWN 

def setup():
    global dataFile
    dataFile = open("data.txt", "w")

def fsm():
        global count
        data = telemetry.telemetry()
        if(len(data)>0):
            dataFile.write(data + "\n")
            type = parse(data)
            if(type != UNKNOWN):
                print(data)
                data = data[4:]
                if(gearth.is_coordinate(data)):
                    gearth.gearth(data)
            else:
                print("Unknown data: "+data)
            if(count > 10):
                print(telemetry.get_rssi())
                count = 0
            time.sleep(0.25)
            count = count + 1
         
def run():
    print("Run called")
    setup()
    telemetry.initialize(COM_PORT)
    gearth.initialize()
    while 1:
        fsm()


if __name__ == "__main__":
    run()

