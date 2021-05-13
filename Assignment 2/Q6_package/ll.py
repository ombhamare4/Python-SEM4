from Q6 import repeatLL
def linked_list():  
    lst=[]
    num1=int(input("Enter Element in linked list...")) 
    for i in range(num1):
        x=int(input())
        lst.append(lst)
    repeatLL(lst)
    return lst

def add(lst):
    num=int(input("Enter Element add to Linked list"))
    lst.append()

def addAnyLL(lst):
    num1=int(input("Enter Index where to add element: "))
    num2=int(input("Enter element to add Linked lst: "))
    lst.insert(num1,num2)
    
def removeLL(lst):
    num=int(input("Enter Element to remove: "))
    lst.remove(num)
  

def replaceLL(lst):
    num1=int(input("Enter Element to Old value "))
    index=lst.index(num1)
    num2=int(input("Enter Element to New value "))
    lst.insert(index,num2)
    lst.remove(num1)



def searchLL(lst):
    num=int(input("\nEnter Number to search: "))
    if num in range(len(lst)):
        print("Number is present at index: {0}".format(lst.index(num)))
    else:
        print("Number is not present")
    

def showLL(lst):
    print("Linked lst: ",lst)
    