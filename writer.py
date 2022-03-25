import serial
import os											#for os.path
import time
import xml.etree.ElementTree as ET			#for parsing the xml files (kml files are xml)


FILE_NAME = "trajectory.kml"			#output kml file
TEMPLATE = "kmlTemplate.kml"			#kml template file (contains formatting but not coord data)

#step 1: open lora serial connection to read recieved gps data
#lora = serial.Serial("/dev/ttyUSB0", 115200)

while (not os.path.exists("coords.txt")):
	print("coords.txt not found...waiting")
	time.sleep(1)
dataFile = open("coords.txt", "r")

#step 2: parse the kml template for the "coordinates" tag
tree = ET.parse(TEMPLATE)
root = tree.getroot()
coordinates = None
for matchingTag in root.iter("{http://www.opengis.net/kml/2.2}coordinates"):
	coordinates = matchingTag

#step 3 continuously read lora data and append it to kml file
coordinates.text = ""
tree.write(FILE_NAME)
while(1):
	try:
		data = dataFile.readline().strip().split(",")
		if(len(data) == 3):
			lat = str(float(data[0]))					#redundant conversion to make sure no transmission error
			lon = str(float(data[1]))
			alt = str(float(data[2])+300.0)
			kmlCoordLine = lon + "," + lat + "," + alt + "\n"
			print (kmlCoordLine.strip())
			coordinates.text = coordinates.text + kmlCoordLine
			tree.write(FILE_NAME)
	except Exception as e:
		print(e)

