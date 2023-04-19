import os
import mmap
import struct
import time

class SharedData:
  def __init__(self):
    self.value = 0

def main():
  # Open shared memory segment for read-only access
  fd = os.open("/my_shared_memory", os.O_RDONLY)
  if fd == -1:
    print("Failed to open shared memory segment.")
    return 1

  # Set size of shared memory segment
  size = struct.calcsize("i")

  

  # Read data from shared memory
  data = SharedData()
  prev_value = data.value

  while True:
    # Map shared memory segment into current process
    addr = mmap.mmap(fd, size, mmap.MAP_SHARED, mmap.PROT_READ)

    data.value = struct.unpack("i", addr.read(size))[0]

    # Check if the value has changed
    if data.value != prev_value:
      print("Value changed to:", data.value)
      prev_value = data.value

if __name__ == "__main__":
  main()