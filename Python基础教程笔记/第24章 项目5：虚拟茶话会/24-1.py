# 一个极简的服务器程序
from asyncore import dispatcher
import asyncore


class ChatServer(dispatcher):
    pass


s = ChatServer()
asyncore.loop()
