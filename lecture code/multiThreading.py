from threading import *
import threading
import time
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


print("8 May 2021")
#8 May 2021
def s1(n):
    for i in n:
        print(i)
    pass

def s2(m):
    for i in m:
        print(i)
n=[1,2,3,4]
m=['a','b','c','d']
t1=Thread(target=s1,args=(n,))
t2=Thread(target=s2,args=(m,))
t1.start()
t2.start()
t1.join


def s3(n):
    for i in n:
        print(i*10)
    pass

def s4(n):
    for i in n:
        print(i*100)
n=[1,2,3,4]
m=['a','b','c','d']
s=time.time()
s3(n)
s4(n)
e=time.time()
print(e-s)
print("Using Threading...")

def s3(n):
    for i in n:
        print(i*10)
    pass

def s4(n):
    for i in n:
        print(i*100)
n=[1,2,3,4]
m=['a','b','c','d']
s=time.time()
t1=Thread(target=s3,args=(n,))
t2=Thread(target=s4,args=(n,))
t1.start()
t2.start()
t1.join()
e=time.time()
print(e-s)

