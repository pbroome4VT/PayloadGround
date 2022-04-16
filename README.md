# Payload 2022

Rocketry@VT
 
Author: Paul Broome

Email: pbroome4@vt.edu

Software for Rocketry@VT Payload 2022. Run on a ground computer to recieve and record data from the payload executing the matchig payload repoitory. In its current phase, it recieves lora packets via a lora tranciever connected via usb. This data is then logged, and parsed to a .kml file. To view live 3-D trajectory, open google earth and import the liveTrajectory.kml file.

## Installation Instructions  Linux(command line)

### Prerequisites
Some software may need to be installed for program to run properly. The following must be installed on the system to proceed.

git

> git --version

If no version is currently installed,
install by running the following command

> sudo apt-get install git
 

python3  should also be installed by default. Again this can be checked by

> python3 --version

and installed by runnning

>sudo apt-get install python3


pip3 must be installed and is likely not installedbe by default. To install, run

> sudo apt-get install python3-pip
 
## Payload Software
Install the payload software by entering

> git clone https://github.com/pbroome4VT/Rocketry-VTPayloadGround.git

> pip3 install -r requirements.txt


## Installation Instructions Windows (command line)
### Prerequisites
Some software may need to be installed or added to the windows PATH environment variable. The following must be installed on the system to proceed.

    python3  should also be installed by default
    git most likely not installed.
    pip3 must be installed
 
 
### Payload Software
Install the payload software by entering

> git clone https://github.com/pbroome4VT/Rocketry-VTPayloadGround.git

> pip3 install -r requirements.txt

#### IMPORTANT!!
    It is likely, you must edit the reciever.py file! The line near the top of the file that creates the variable SERIAL_PORT must be changed to the serial port assigned to the lora tranciever usb. 
    
    On linux this string should be "/dev/ttyUSBx" followed by a number instead of the letter 'x'. The easiest way to
    find this is to navigate to the directroy and see which device file appears/disappears when you plug in the usb.
    It is most likely "/dev/ttyUSB0".
    
    On windows This string should "COMx" with a number instead of the letter 'x'. You will need to find the COM port
    assosicated with the usb connection. This can be done by opening the device manager, navigating the to the view menu
    option and selecting "show hidden devices". Then navigate to the COM ports device folder and determine which com
    port corresponds to the usb by plugging and unplugging the device.



## Usage
After intalling, the program can be run by executing the corresponding payload.sh bash file.

On linux that means, run linuxPayload.sh

on windows, that means, run windowsPayload.sh
