#Om Ghanshyam Bhamare SE A 3
#Assignmet 2
#A Python program where two threads are acting on the same method to allot a berth for the passenger
import threading
from threading import Thread, Lock
import time
lock = threading.Lock()

def allotment(lock):
  while True:
    if lock.acquire(blocking=False) is True:
      break
    else:
      print("Not Available")
      time.sleep(0.1)
    lock.release()
    print("Allotment Vacant")

p1=Thread(target=allotment,args=(lock,))
p2=Thread(target=allotment,args=(lock,))

p1.start()
p2.start()
p1.join()
p2.join()