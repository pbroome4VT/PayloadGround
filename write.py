import sys
import os.path
from GEarth import gearth

def main():
    args = sys.argv[1:]
    if(len(args) == 1):
        if(os.path.exists(args[0])):
            gearth.initialize()
            file = open(args[0])
            data = file.readline()
            while(data != ""):
                gearth.gearth(data)
                data = file.readline()
            print("finished writing")
        else:
            print("Error: couldnt find file: "+args[0])
    else:
        print("ERROR requires single arguement that is coords file path")

if __name__ == "__main__":
    main()