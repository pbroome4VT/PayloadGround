import serial
import time
from Telemetry import constants as c


tranceiver = None


def initialize_telemetry(port):
    global tranceiver
    tranceiver = serial.Serial(port=port, baudrate=c.BAUD_RATE, timeout=c.READ_TIMEOUT, write_timeout=c.WRITE_TIMEOUT)
    if(tranceiver.is_open):
        tranceiver.write(b"+++")
        time.sleep(2)
        tranceiver.write(b"ATI\r")
        time.sleep(0.1)
        tranceiver.write(b"AT&F\r") #reset to factor default
        time.sleep(0.1)
        #tranceiver.write(b"ATS3=111\r") #set register 3 (network id) to 111
        time.sleep(0.1)
        #tranceiver.write(b"ATS15=1\r") #set register 15(node id) to 1
        time.sleep(0.1)
        #tranceiver.write(b"ATS9=916,000\r") # set register9 (max freq) to 9.16 Mhz
        time.sleep(0.1)
        #tranceiver.write(b"ATS4=10\r") #set register 4(tx power) to 20db
        time.sleep(0.1)
        tranceiver.write(b"AT&W\r") #write parameters
        time.sleep(0.1)
        tranceiver.write(b"ATZ\r") #reboot modem
        time.sleep(0.3)
    else:
        print("ERROR opening tranceiver serial UART5")

        
def transmit(msg):
    global tranciever
    msg = str(msg) + "\r\n"
    n = 0
    try:
        n = tranceiver.write(msg.encode('utf-8'))
    except serial.SerialTimeoutException:
        pass
    return n

def telemetry():
    global tranciever
    data = tranceiver.readline()
    try:
        data = data.decode("utf-8").strip()
        if(len(data)>0):
            print(data)
            return data
    except:
        pass
    return None