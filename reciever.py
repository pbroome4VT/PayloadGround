#!/usr/bin/env python3

#Author: Paul Broome
#Data: 3/13/22
#Description: Recieves data from a lora tranciever connected to computer serial port.
#	Sets lora reciever to network 6 and ID 2 since the transmitter is assumed to be on network #6
#	and transmitting to reciever with ID #2.
#	It's assumed that the tranciever is connected to serial port /dev/ttyUSB0 (THIS MAY NOT BE THE CASE!)
import serial

#MUST CHANGE DEPENDING ON WINDOWS/MAC
#LINUX will be "/dev/ttyUSB<x>" which is most likely "/dev/ttyUSB0"
#WINDOWS will be "COM<x>" where you will have to determine which COM port. For example, "COM3" if it connected to com port 3.  
SERIAL_PORT = "/dev/ttyUSB0"


def loraReadLine():
	string = ""
	try:
		string = lora.readline().decode("UTF-8").strip()
	except Exception as e:
		print(e)
	return string


print("reciever.py called")
lora = serial.Serial(SERIAL_PORT, 115200)
if not lora.isOpen():
	print("lora failed to open")
coords_file = open("coords.txt", "w")

lora.write("AT+NETWORKID=6\r\n".encode())
print("AT+NETWORKID=6: ", loraReadLine())

lora.write("AT+ADDRESS=2\r\n".encode())
print("AT+ADDRESS=2: ", loraReadLine())

#assign lora Paramaters
lora.write("AT+PARAMETER=12,4,1,7\r\n".encode())
print("AT+PARAMETER=12,4,1,7: ", loraReadLine())

while(1):
	try:
		data = loraReadLine()[5::].split(",")
		if (len(data) == 7):
			address = data[0]
			length = data[1]
			data_lat = str(float(data[2]))
			data_lon = str(float(data[3]))
			data_alt = str(float(data[4]))
			rssi = data[5]
			snr = data[6]
			if(float(data_lat) == -1 or float(data_lon) == -1 or float(data_alt) == -1):
				print("no fix")
			else:
				print("address: " + address + "\nlength: " + length + "\nLatitude: " + data_lat + "\nLongitude: "+data_lon +"\nAltitude: " + data_alt + "\nRSSI: " + rssi + "\nSNR: "+snr)
				coords_file.write(data_lat + "," + data_lon +","+data_alt+"\n")
				coords_file.flush()
	except Exception as e:
		print(e)
