import socket
# -------------------------------------------------------
socket.socket()

# 参数
# family:
# socket.AF_INET    IPv4(默认)
# socket.AF_INET6   IPv6
# socket.AF_UNIX    用于单一的Unix系统进程间通信

# type:
# SOCK_STREAM    流式socket TCP协议（默认）
# SOCK_DGRAM     数据报式socket UDP协议
# SOCK_RAW       原始套接字
# SOCK_RDM       可靠UDP
# SOCK_SEQPACKET 可靠的连接数据包服务
#--------------------------------------------------------

# 获取tcp/ip套接字
tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取udp/ip套接字
udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 由于 socket 模块中有太多的属性。我们在这里破例使用了'from module import *'语句。使用 'from socket import *',我们就把 socket 模块里的所有属性都带到我们的命名空间里了,这样能 大幅减短我们的代码。
# 例如tcpSock = socket(AF_INET, SOCK_STREAM)

#----------------------------------------------------------
# 套接字对象内建方法
# 服务端套接字函数
s.bind()           # 绑定(主机,端口号)到套接字
s.listen(5)        # 开始TCP监听, 5为最大连接数
s.accept()         # 被动接受TCP客户的连接,(阻塞式)等待连接的到来

# 客户端套接字函数
s.connect()        # 主动初始化TCP服务器连接
s.connect_ex()     # connect()函数的扩展版本,出错时返回出错码,而不是抛出异常

# 公共用途的套接字函数
s.recv(1024)       # 接收TCP数据,1024为一次数据接收大小
s.send()           # 发送TCP数据(send在待发送数据量大于己端缓存区剩余空间时,数据丢失,不会发完),数据格式bytes
s.sendall()        # 发送完整的TCP数据(本质就是循环调用send,sendall在待发送数据量大于己端缓存区剩余空间时,数据不丢失,循环调用send直到发完)
s.recvfrom()       # 接收UDP数据
s.sendto()         # 发送UDP数据
s.getpeername()    # 连接到当前套接字的远端的地址
s.getsockname()    # 当前套接字的地址
s.getsockopt()     # 返回指定套接字的参数
s.setsockopt()     # 设置指定套接字的参数
s.close()          # 关闭套接字

# 面向锁的套接字方法
s.setblocking()    # 设置套接字的阻塞与非阻塞模式
s.settimeout()     # 设置阻塞套接字操作的超时时间
s.gettimeout()     # 得到阻塞套接字操作的超时时间

# 面向文件的套接字的函数
s.fileno()         # 套接字的文件描述符
s.makefile()       # 创建一个与该套接字相关的文件
