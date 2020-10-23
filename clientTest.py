import socket

s = socket.socket()
host = '192.168.99.160'
port = 12345
s.connect((host, port))
#print(s.recv(1024))
print(s.recv(1024).decode('utf-8'))
s.close()
