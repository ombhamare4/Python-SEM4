#Create server 
import socket
import sys
#step 1


#step 2
#bind to host and port number
#Only take one parameter but need to pass two element
host = 'localhost'
port = 5000
s=socket.socket()
s.bind((host,port))

# step 3 :
#how many client i can connect at single point of time
s.listen(1)

#accept to client
#accept return two values 
#here c is port number and addr are IP address
c,addr=s.accept()
print("Client has accepted the connection")

#next step is sending msg
#in this we are receving file and sending it
#we will ask the client name of file to receieve
#recv function store the something recevie from client 
fname=c.recv(1024)#1024 is buffer

#the information recevive in form of bytes so we have to convert into string
fname=str(fname.decode())
#print the name of file
print("File name recevied from client ",fname)

#open read file
f=open(fname,'rb')#open file
contents=f.read()#store in variable

c.send(contents)
print("File contents sent...")


c.close()#close the connection