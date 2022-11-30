import os
import time

GEARTH_DIR = os.path.dirname(os.path.abspath(__file__))        #GEarth module folder
GEARTH_DATA_DIR = GEARTH_DIR + "/Data"
LOG_FILE_TIMESTAMP = time.strftime("%b_%d_%H_%M_%S")
COORDS_FILE = GEARTH_DATA_DIR + "/coords" + LOG_FILE_TIMESTAMP 
TEMPLATE_FILE = GEARTH_DIR + "/kmlTemplate.kml"
TRAJECTORY_KML = GEARTH_DIR + "/trajectory.kml"