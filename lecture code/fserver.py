import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',8452))
s.listen(1)
c,add=s.accept()
print("Connection established from:",str(add),str(c))
c.send(b'Hello!!,This is server')
c.close()

