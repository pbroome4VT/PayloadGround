#Author: Paul Broome
#Data: 3/13/22
#Description: Recieves data from a lora tranciever connected to computer serial port.
#	Sets lora reciever to network 6 and ID 2 since the transmitter is assumed to be on network #6
#	and transmitting to reciever with ID #2.
#	It's assumed that the tranciever is connected to serial port /dev/ttyUSB0 (THIS MAY NOT BE THE CASE!)
import serial

def loraReadLine():
	return lora.readline().decode("UTF-8").strip()[5::]


lora = serial.Serial("/dev/ttyUSB0", 115200)
if not lora.isOpen():
	print("lora failed to open")
coords_file = open("coords.txt", "w")

lora.write("AT+NETWORKID=6\r\n".encode())
print("AT+NETWORKID=6: ", loraReadLine())

lora.write("AT+ADDRESS=2\r\n".encode())
print("AT+ADDRESS=2: ", loraReadLine())


while(1):
	data = loraReadLine().split(",")
	if (len(data) == 7):
		address = data[0]
		length = data[1]
		data_lon = data[2]
		data_lat = data[3]
		data_alt = data[4]
		rssi = data[5]
		snr = data[6]
		print("address: " + address + "\nlength: " + length + "\nLatitude: " + data_lat + "\nLongitude: "+data_lon +"\nAltitude: " + data_alt + "\nRSSI: " + rssi + "\nSNR: "+snr+"\n")
		coords_file.write(data_lat+","+data_lon+","+data_alt+"\n")
		coords_file.flush()
