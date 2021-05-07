from threading import *
import threading
#Threading methods
#getName()
#current_thread()...display current thread name

print(current_thread().getName()) 

def sample():
    print("Child Thread")
child=Thread(target=sample)
child.start()
print(current_thread().getName())

print("")

class mythread(threading.Thread):
    def run(self):
        for i in range(3):
            print("Hello All")

t=mythread()
t.start()
t.join()
print(current_thread().getName()) 

print("")

class Example:
    def fun(self):
        for i in  range(3):
            print("Hello All two")

obj=Example()
t1=Thread(target=obj.fun)
t1.start()
t1.join()
