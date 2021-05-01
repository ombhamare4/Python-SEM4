#Assign 1 (3): 
#A Python program to accept 3 integers 
#separated by commas and display their average.
#Om Ghanshyam Bhamare Div A Roll No: 3
numbers = input("Input some comma seprated numbers : ")
list = numbers.split(",")
sum1=0
for x in list:
    sum1=sum1+int(x)

avg=sum1/len(list)
print("Total sum: "+str(sum1))
print("Total numbers: "+str(len(list)))
print(avg)
