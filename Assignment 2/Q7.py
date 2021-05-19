#Om Ghanshyam Bhamare SE A 3
#Assignmet 2
#A Python program where two threads are acting on the same method to allot a berth for the passenger
import threading

trd = threading.Thread()

def allotment(trd):
    while True:
        if trd.acquire(blocking=False) is True:
            break
        else:
            print("Not available")
            # time.sleep(0.1)
        print("Seat Allowed")
        trd.release()
        print("Allotment Vacant")


t1=Thread(target=allotment,args=(trd,))
t2=Thread(target=allotment,args=(trd,))

t1.start()
t2.start()
t1.join()
t2.join()