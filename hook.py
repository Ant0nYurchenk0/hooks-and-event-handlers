import struct

f = open("/dev/input/event2", "rb")
counter = 0
while 1:
  data = f.read(24)
  unpack = struct.unpack('4IHHI', data)
  counter+=1
  if(counter==2 and int(unpack[6])==1):
    print(unpack[5])
  if(counter==3):
    counter=0