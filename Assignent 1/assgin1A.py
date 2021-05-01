#Assign 1 (1):
#A Python program to convert numbers from octal, binary and 
# hexadecimal systems into decimal number system.
#Om Ghanshyam Bhamare Div A Roll No: 3
#Binary to decimal
binNum=10110
decimal,i,n=0,0,0
while(binNum!=0):
    rem=binNum%10
    decimal+=rem*pow(2,i)
    binNum//=10
    i+=1
print("Binary to decimal: "+str(decimal))

#Octal to decimal
octNum=24
decimal1,base=0,1
while(octNum):
    last_digit=octNum%10
    octNum=int(octNum/10)
    decimal1+=last_digit*base
    base=base*8
print("Octal to Decimal: "+str(decimal1))

#HexaDecimal to decimal
hexaNum="4A7F"
chk=0
decnum=0
hexlen=len(hexaNum)
hexlen=hexlen-1
i=0
while hexlen>=0:
    rem=hexaNum[hexlen]
    if rem>='0' and rem<='9':
        rem=int(rem)
    elif rem>='A' and rem<='F':
        rem=ord(rem)
        rem=rem-55
    elif rem>='a' and rem<='f':
        rem=ord(rem)
        rem=rem-87
    else:
        chk=1
        break
    decnum+=(rem*(16**i))
    hexlen-=1
    i+=1
if chk==0:
    print("Hexadecimal To Decimal: "+str(decnum))