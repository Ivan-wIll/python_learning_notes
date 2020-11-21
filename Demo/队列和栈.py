# 队列: 先进先出
# 栈: 后进先出

# 两个类Queue(队列),Stack(栈)
# 两个方法put(放)和get(取)
# 继承关系


# 方法一
class Queue:
    def __init__(self):
        self.list = []

    def put(self, n):
        self.list.append(n)

    def get(self):
        return self.list.pop(0)


class Stack():
    def __init__(self):
        self.list = []

    def put(self, n):
        self.list.append(n)

    def get(self):
        return self.list.pop()


# ------------------------------------------------------
# 方法二
# 继承
class Foo:
    def __init__(self):
        self.list = []

    def put(self, n):
        self.list.append(n)

    def get(self):
        return self.list.pop() if self.index else self.list.pop(0)


class Queue1(Foo):
    def __init__(self):
        self.index = 0
        Foo.__init__(self)


class Stack1(Foo):
    def __init__(self):
        self.index = 1
        Foo.__init__(self)


# -----------------------------------------------

a = Queue()
a.put(1)
a.put(2)
a.put(3)
print(a.get())
b = Stack()
b.put(1)
b.put(2)
b.put(3)
print(b.get())
print(b.get())
print(b.get())
print(b.get())
len