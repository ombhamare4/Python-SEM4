#Om Ghanshyam Bhamare SE A 3
#Assignmet 2
#A Python program to create a package using data 
# structures for a linked list and perform and use all the
#operations.
def info():
    print("Watashi no name om Desu")

def linkedlist():
    choice=0
    ll=[]
    while(choice!=8):
        print("Linked List\nSelect Operation\n1]Traverse\t2]Append\n3]Insert\t4]Remove\n5]Replace\t6]Search\n7]Length\t8]Exit\n\n")
        choice=int(input("Enter Your Choice...: "))
        if choice==1:
            for i in ll:
                print(i)
        if choice==2:
            a = input("Enter Element in Linked list: ")
            b = a.split()
            for i in range(len(b)):
                # ll[i]=int(ll[i])
                ll.append(int(b[i]))
            print(ll)
        if choice==3:
            a=int(input("Enter Postion: "))
            b = int(input("Enter Element: "))
            ll.insert(a,b)
        if choice==4:
            if ll==[]:
                print("Linked List is Empty: ")
            else:
                a = int(input("Enter Element to remove: "))
                ll.remove(a)
        if choice==5:
            n =int(input("Enter the Element to Remove: "))
            b=int(input("Enter New Element: "))
            if n in ll:
                i=ll.index(n)
                ll.pop(i)
                ll.insert(i,b)
        if choice==6:
            a=int(input("Eneter Element to search: "))
            if a in ll:
                print("Element found...")
            else:
                print("Element Not Fouund...")
        if choice==7:
            length=len(ll)
            print(length)
        if choice==8:
            break

