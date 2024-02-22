import serial
import time
from Telemetry import constants as c


tranceiver = None

def read_modem():
    global tranciever
    data = tranceiver.readline()
    try:
        data = data.decode("utf-8").strip()
        if(len(data)>0):
            pass
            #print(data)
    except:
        data = ""
    return data

def flush_modem():
    while(read_modem() != ""):
        pass

#put in the cmd string and a pattern to match for an acknowledge string
#if acknowledged, it will return the string. if unable to acknowledge, returns ""
def send_cmd(cmd_str, ack_str):
    global tranceiver
    ret = ""
    flush_modem()
    tranceiver.write(cmd_str.encode("utf-8"))
    if(ack_str != ""):
        tranceiver.timeout = 0.1
        for index in range (0, 20):
                reply = read_modem()
                if(reply.__contains__(ack_str)):
                    ret = reply
                    break
        tranceiver.timeout = c.READ_TIMEOUT
    return ret

def enter_cmd_mode():
    reply = send_cmd("+++", "OK")
    return len(reply) > 0

def exit_cmd_mode():
    global tranceiver
    send_cmd("ATO\r", "")


def get_rssi():
    enter_cmd_mode()
    reply = send_cmd("ATI7\r", "RSSI")
    ret = ""
    if(len(reply) > 0):
        ret = reply
    exit_cmd_mode()
    return ret

def initialize_telemetry(port):
    global tranceiver
    tranceiver = serial.Serial(port=port, baudrate=c.BAUD_RATE, timeout=c.READ_TIMEOUT, write_timeout=c.WRITE_TIMEOUT)
    if(tranceiver.is_open):
        enter_cmd_mode()
        tranceiver.write(b"ATI\r")
        time.sleep(0.1)
        tranceiver.write(b"AT&F\r") #reset to factor default
        time.sleep(.1)
        #tranceiver.write(b"ATS3=111\r") #set register 3 (network id) to 111
        time.sleep(0.1)
        #tranceiver.write(b"ATS9=916,000\r") # set register9 (max freq) to 9.16 Mhz
        time.sleep(0.1)
        tranceiver.write(b"ATS4=30\r") #set register 4(tx power) to 20db
        time.sleep(0.1)
        tranceiver.write(b"ATS2=64\r")#set air data rate to 64(not sure exactly what this means but has to do with bytes per second i think)
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
    return read_modem()
    