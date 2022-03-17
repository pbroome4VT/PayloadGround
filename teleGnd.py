
import os
nForks = 2
childNum = 0

i = 1
in_startup = True
while (i <= nForks and in_startup == True):
   newPid = os.fork()
   if newPid == 0:
      in_startup = False
      childNum = i
   else:
      i += 1
if (childNum == 0):
   ##if startup program, stall forever
   while True:
      pass
elif (childNum == 1):
   print("calling gps.py")
   os.execlp("python3", "python3", "reciever.py")
elif(childNum == 2):
   print("calling transmitter.py")
   os.execlp("python3", "python3", "writer.py")
