import os
import mmap
import struct
import time

class SharedData:
  def __init__(self):
    self.value = 0

def main():
  # Open shared memory segment for read and write
  fd = os.open("/my_shared_memory", os.O_CREAT | os.O_RDWR)
  if fd == -1:
    print("Failed to create shared memory segment.")
    return 1

  # Set size of shared memory segment
  size = struct.calcsize("i")

  # Truncate segment to appropriate size
  os.ftruncate(fd, size)


  # Write data to shared memory
  data = SharedData()
  counter = 0
  while(True):
    # Map shared memory segment into current process
    addr = mmap.mmap(fd, size, mmap.MAP_SHARED, mmap.PROT_WRITE)

    data.value = counter
    addr.write(struct.pack("i", data.value))
    print(f"New value: ", data.value)

    # Wait for a while to simulate some processing time
    time.sleep(2)
    counter+=1

    # Unmap shared memory segment
    addr.close()

  # Close shared memory file descriptor
  os.close(fd)

if __name__ == "__main__":
  main()