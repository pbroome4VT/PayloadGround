#SERIAL_PORT = "COM12"
import time
from Telemetry import telemetry
from GEarth import gearth

count = 0

def setup():
    pass

def fsm():
        global count

        data = telemetry.telemetry()
        gearth.gearth(data)
        if(count > 50):
            print(telemetry.get_rssi())
            count = 0
        
        time.sleep(0.25)
        count = count + 1
         
def run():
    print("Run called")
    setup()
    telemetry.initialize("COM3")
    gearth.initialize()
    while 1:
        fsm()
        
    


if __name__ == "__main__":
    run()

