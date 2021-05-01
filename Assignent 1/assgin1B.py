#Assign 1 (2): 
#A Python program to convert numbers from octal, binary and hexadecimal 
# systems into decimal number system using int() function 
#(Take input from user)
#Om Ghanshyam Bhamare Div A Roll No: 3
#Binary to decimal
binNum=int(input("Enter Number only in binary: "))
binStr=str(binNum)
p=set(binStr)
s={'0','1'}
if s==p or p=={'0'} or p=={'1'}:
    decimal,i,n=0,0,0
    while(binNum!=0):
        rem=binNum%10
        decimal+=rem*pow(2,i)
        binNum//=10
        i+=1
    print("Binary to decimal: "+str(decimal))
else:
    print("Sorry can't converted Plz check input...")
#Octal to decimal
octNum=int(input("Enter Number only in Octal: "))
decimal1,base=0,1
while(octNum):
    last_digit=octNum%10
    octNum=int(octNum/10)
    decimal1+=last_digit*base
    base=base*8
print("Octal to Decimal: "+str(decimal1))

#HexaDecimal to decimal
hexaNum=int(input("Enter Number only in Hexa: "),16)
print("Hex to decimal: "+str(hexaNum))
