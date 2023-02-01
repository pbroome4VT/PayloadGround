import xml.etree.ElementTree as ET
import os
from GEarth import constants as c

#global variables
#-----------------------------------
coordsFile = None
#kml variables
tree = None
root = None
coordTag = None

def is_float(text):
    try:
        float(text)
        return True
    except ValueError:
        return False

def initialize_environment():
    #print("gps_init_env called")
    #create data direcory for logging if it doesnt already exist
    if(not os.path.exists(c.GEARTH_DATA_DIR)):
        os.mkdir(c.GEARTH_DATA_DIR)

    global coordsFile
    coordsFile = open(c.COORDS_FILE, "w")

    
def initialize_gearth():
    global tree
    global root
    global coordTag
    tree = ET.parse(c.TEMPLATE_FILE)
    root = tree.getroot()
    for matchingTag in root.iter("{http://www.opengis.net/kml/2.2}coordinates"):
	    coordTag = matchingTag


def is_coordinate(data):
    try:
        data = data.strip().split(" ")
        if(len(data) == 3):
            if(is_float(data[0]) and is_float(data[1]) and is_float(data[2])):
                if(abs(float(data[0])) < 90 and abs(float(data[1])) < 180):
                    return True
    except: 
        pass
    return False


def gearth(data):
    if(is_coordinate(data)):
        global coordsFile
        data = data.strip() + "\n"
        coordsFile.write(data)

        data = data.split(" ")
        lat = data[0]					#redundant conversion to make sure no transmission error
        lon = data[1]
        alt = str(float(data[2]))
        kmlCoordLine = lon + "," + lat + "," + alt + "\n"
        global coordTag
        global tree
        coordTag.text = coordTag.text + kmlCoordLine
        tree.write(c.TRAJECTORY_KML)

        
