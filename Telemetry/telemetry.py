from Telemetry import helper as h


def initialize(port):
    h.initialize_telemetry(port)

def transmit(msg):
    return h.transmit(msg)

def telemetry():
    return h.telemetry()
