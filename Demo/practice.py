import socket

skt = socket.socket()
skt.bind(('127.0.0.1', 9000))  #
skt.listen()

conn, addr = skt.accept()
conn.send(b'Hello')
conn.recv(1024)
conn.close()

skt.close()