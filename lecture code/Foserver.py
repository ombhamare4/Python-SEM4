import socket
s=socket.socket()
print("socket Connected")
s.bind(('localhost',5000))
print("Binded Success...")
s.listen(1)
	
while True:
	c,addr=s.accept()
	c.send(b"Hello plz work")

	c.close()
