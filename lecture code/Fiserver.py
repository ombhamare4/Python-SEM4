import socket
s=socket.socket()
print("Socket Created...")
s.bind(('localhost',5000))
s.listen(1)

c,addr=s.accept()

while True:
	data=c.recv(1024)
	if not data:
		break
	data=str(data.decode())
	print("Client says: "+data)

	data1=input("Enter Something(server): ")
	c.send(data1.encode())

c.close()