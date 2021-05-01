#Exp 1 (a): 
#Om Ghanshyam Bhamare Div A Roll No: 3
my_str=input('Enter a a string: ')
print('string in forward order:')
for i in (my_str):
    print(i,end=" ")
reversed=my_str[::-1]
print('\nstring in reverse order:')
for i in reversed:
    print(i,end=" ")
print(' ')
if my_str==reversed:
    print('Palindrome')
else:
    print('NOT Palindrome')