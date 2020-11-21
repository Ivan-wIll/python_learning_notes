# 服务器端
import socket

# 获取Tcp/ip套接字
skt = socket.socket()  # 默认

# # 获取udp/ip套接字
# udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

skt.bind(('127.0.0.1', 9001))  # 向操作系统申请资源(端口)
skt.listen()

while True:  # 和多个客户端进行握手
    conn, addr = skt.accept()
    print('conn: ', conn)

    while True:
        send_msg = input('>>>')
        conn.send(send_msg.encode('utf-8'))
        if send_msg == 'q':  # 输入q退出会话,断开连接
            break
        msg = conn.recv(1024).decode('utf-8')
        print(msg)
    conn.close()  # 挥手,断开连接

skt.close()  # 归还操作系统资源(断开端口)
