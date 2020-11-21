import socket
import json
import struct
# 接收
skt = socket.socket()
skt.bind(('127.0.0.1', 9001))
skt.listen()

conn, _ = skt.accept()
msg = conn.recv(4)  # 接收固定收4个字节
msg_len = struct.unpack('i', msg)[0]  # 反解出b_dic的总字节数
b_dic = conn.recv(msg_len)  # 接收b_dic数据,
dic = b_dic.decode('utf-8')   # 解码成字符串格式
# json字符串还原为字典模式
dic = json.loads(dic)

with open(dic['filename'], 'wb') as f:
    while dic['filesize'] > 0:
        content = conn.recv(1024)
        dic['filesize'] -= len(content)
        f.write(content)

conn.close()
skt.close()