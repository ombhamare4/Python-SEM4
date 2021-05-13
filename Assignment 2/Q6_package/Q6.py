#A Python program to create a package using data structures for a linked list and perform and use all the
#operations.
from ll import add,addAnyLL,removeLL,replaceLL,searchLL,showLL,linked_list


print("Package Problem...")
repeatLL()

def repeatLL():
    print("1]Create Linked List\n2]Add Element\n3]Add any positon\n4]Remove Linked List\n5]Replace Element\n6]Search \n7]Show")
    n= int(input("Enter Choice"))
    if n==1:
        linked_list()
    elif n==2:
        add()
    elif n==3:
        addAnyLL()
    elif n==4:
        removeLL()
    elif n==5:
        replaceLL()
    elif n==6:
        searchLL()
    elif n==9:
        showLL()
    else:
        print("Plz Enter Valid choice...")
        
