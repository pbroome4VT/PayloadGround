from GEarth import helper as h


def initialize():
    h.initialize_environment()
    h.initialize_gearth()

def gearth(data):
    h.gearth(data)

def is_coordinate(data):
    return h.is_coordinate(data)