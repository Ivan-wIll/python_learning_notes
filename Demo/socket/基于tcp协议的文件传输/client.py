import socket
import os
import json
import struct  # 解决粘包问题
# 发送
skt = socket.socket()
skt.connect(('127.0.0.1', 9001))

# 获取文件名\文件大小
abs_path = r'C:\Users\Ivan\python_learning_notes\Demo\socket\tmp.html'
filename = os.path.basename(abs_path)
filesize = os.path.getsize(abs_path)
dic = {
    'filename': filename,
    'filesize': filesize
}
# 用json将head_dic转化成字符串
str_dic = json.dumps(dic)
b_dic = str_dic.encode('utf-8')  # bytes
# 将b_dic的大小转化成固定的4个字节
ret = struct.pack('i', len(b_dic))  # 固定4个字节
skt.send(ret)  # 发送字典转成字节之后的长度 4个字节
skt.send(b_dic)  # 具体的字典数据

# 发送文件
with open(abs_path, mode='rb') as f:
    while filesize > 0:
        # f1.read() 不能全部读出来，而且也不能send全部，这样send如果过大，
        # 也会出问题，保险起见，每次至多send(1024字节)
        content = f.read(1024)
        filesize -= len(content)
        skt.send(content)

skt.close()