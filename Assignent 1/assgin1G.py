#Assign 1 (7): 
#A Python program to accept a numeric 
# digit from keyboard and display in words.
# (Between 1 to 5)
#Om Ghanshyam Bhamare Div A Roll No: 3

#using dictionary
my_dict={1:"One",2:"Two",3:"Three",4:"Four",5:"Five"}
num=int(input("Enter Number (1 to 5): "))
if num in my_dict:
        print(my_dict[num])
else:
    print("Plz Enter element between 1 to 5")