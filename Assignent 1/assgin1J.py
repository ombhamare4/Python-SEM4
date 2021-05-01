#Assign 1 (10): 
#A Python program to retrieve only negative 
# numbers from a list of numbers.
#A Python program to assert if a 
#user enters a number greater than zero.

#Om Ghanshyam Bhamare Div A Roll No: 3
lst=[-2,5,-22,54,-12,-45,59]
for i in range (len(lst)):
    if lst[i]<0:
        print(lst[i])

num=int(input("Enter Number: "))
#Use of assertion
# An assertion is a sanity-check that 
# you can turn on or turn off when you are 
# done with your testing of the program.
assert num < 0,'you enter value greater than zero'

