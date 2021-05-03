

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('localhost',8452))
msg = s.recv(1024)
while msg:
    print("Recieved: ",msg.decode())
    msg = s.recv(1024)
s.close()