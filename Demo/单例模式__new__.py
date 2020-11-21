# __new__

# 类实例化的时候
# 先创建一块对象的空间，有一个指针指向类 --> __new__
# 再调用init --> __init__


# 设计模式 -- 单例模式
# 一个类, 从头到尾, 只会创建一次self的空间
class Baby:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, cloth, pants):
        self.cloth = cloth
        self.pants = pants


b1 = Baby("红毛衣", "绿皮裤")
print(b1.cloth)
b2 = Baby("白衬衫", "黑牛仔")
print(b1.cloth)
print(b2.cloth)

# 其他例子: 模块导入...