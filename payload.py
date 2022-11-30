#SERIAL_PORT = "COM12"
import time
from Telemetry import telemetry
from GEarth import gearth

def setup():
    pass

def fsm():
        data = telemetry.telemetry()
        gearth.gearth(data)
        time.sleep(.25)
         
def run():
    print("Run called")
    setup()
    telemetry.initialize("COM12")
    gearth.initialize()
    while 1:
        fsm()
        
    


if __name__ == "__main__":
    run()

