#Assign 1 (4):
#A Python program to accept a group 
#of strings separated by commas and display them again.
#Om Ghanshyam Bhamare Div A Roll No: 3
numbers = input("Input some comma seprated numbers : ")
list = numbers.split(",")
for x in list:
    print(x)
print(list)