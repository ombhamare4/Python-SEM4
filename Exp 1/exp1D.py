#Exp 1 (d): Write a program in python to implement FizzBuzz 
#Om Ghanshyam Bhamare Div A Roll No: 3

for i in range(1,21):
    if i%3==0:
        print("Fizz",end="")
    if i%5==0:
        print("Buzz",end="")
    if (i%3!=0 and i%5!=0):
        print(i ,end="")
    print()
