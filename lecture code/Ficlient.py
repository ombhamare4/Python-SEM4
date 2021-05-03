import socket
s=socket.socket()
s.connect(('localhost',5000))
data=input("Enter Anything(Client): ")
while data!="exit":
	s.send(data.encode())

	data1=s.recv(1024)
	data1=data1.decode()
	print("Server Says: "+data1)

	data=input("Enter Anything: ")
	

s.close()