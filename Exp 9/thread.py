#Om Ghanshyam Bhamare SE A 3
#Exp 9: Programs on Threading using python.
import threading
def sum_print(num1,num2):
    sum1=num1+num2
    print("Sum is "+str(sum1))

def diff_print(num1,num2):
    diff1=num1-num2
    print("Difference is "+str(diff1))

t1=threading.Thread(target=sum_print,args=(30,5,))
t2=threading.Thread(target=diff_print,args=(25,5,))

t1.start()
t2.start()
t1.join()
t2.join()