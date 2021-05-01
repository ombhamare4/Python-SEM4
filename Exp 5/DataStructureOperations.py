
def sum1(a,b):
    return a+b

def sub1(a,b):
    return a-b
    
choice = int(input("Enter your choice: "))

if choice==1:
    num1=int(input("Enter First Number: "))
    num2=int(input("Enter Second Number: "))  
    print(sum1(num1,num2))
elif choice==2:
    num1=int(input("Enter First Number: "))
    num2=int(input("Enter Second Number: "))  
    print(sub1(num1,num2))
else:
    print("Enter Proper input: ")

