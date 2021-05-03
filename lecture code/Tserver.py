import socket
s=socket.socket()
print("Socket created...")

s.bind(('localhost',5000))
print("Binded Successfully...")

s.listen(1)
print("Waiting for Connection...")

while True:
    c,addr=s.accept()
    print("Connected with ",addr)
    c.send(b"Hello")

    c.close()

print("Passeddd...")

# c.close()