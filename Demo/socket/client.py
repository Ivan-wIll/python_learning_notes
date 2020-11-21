import socket

skt = socket.socket()
skt.connect(('127.0.0.1', 9001))

while True:
    msg1 = skt.recv(1024)
    msg2 = msg1.decode('utf-8')
    if msg2 == 'q':
        break
    print(msg1, msg2)
    send_msg = input('>>>')
    skt.send(send_msg.encode('utf-8'))
    if msg2 == 'q':
        break
skt.close()
