#Assign 1 (13): 
#A Python program to multiply all
# the numbers in a list using functions.

#Om Ghanshyam Bhamare Div A Roll No: 3

def cal(lst):
    product=1
    for x in lst:
        product*=x
    print("Total Product of list is: "+str(product))

lst=[1,2,3,4]
cal(lst)