import socket

s = socket.socket()
host = '192.168.99.160'
port = 12345
s.bind((host, port))

s.listen(5)
while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  c.send('Thank you for connecting'.encode('utf-8'))
  c.close()
