from Telemetry import helper as h


def initialize(port):
    h.initialize_telemetry(port)

def transmit(msg):
    return h.transmit(msg)

def get_rssi():
    return h.get_rssi()
    
def telemetry():
    return h.telemetry()
