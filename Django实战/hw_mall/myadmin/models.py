from django.db import models


# Create your models here.
class Users(models.Model):
    """用户信息表"""
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    sex = models.IntegerField(default=1)
    address = models.CharField(max_length=100)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    state = models.IntegerField(default=1)
    update_time = models.DateTimeField(auto_created=True, auto_now=True)
    create_time = models.DateTimeField(auto_created=True, auto_now_add=True)

    class Meta:
        db_table = 'users' # 更改表名


class Types(models.Model):
    """商品类别表"""
    name = models.CharField(max_length=32)
    pid = models.IntegerField(default=0)
    path = models.CharField(max_length=255)

    class Meta:
        db_table = 'type'


class Goods(models.Model):
    """商品信息数据表"""
    typeid = models.IntegerField()
    goods = models.CharField(max_length=32)
    company = models.CharField(max_length=50)
    descr = models.TextField()
    price = models.FloatField()
    picname = models.CharField(max_length=255)
    state = models.IntegerField(default=1)
    store = models.IntegerField(default=0)
    num = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    addtime = models.IntegerField()

    class Meta:
        db_table = "goods"


class Orders(models.Model):
    """订单信息表"""
    uid = models.IntegerField()
    linkman = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    addtime = models.IntegerField()
    total = models.FloatField()
    status = models.IntegerField()

    class Meta:
        db_table= "orders"


# class Detail(models.Model):
#     """详情表"""
#     orderid = models.IntegerField()
#     goodsid = models.IntegerField()
#     name = models.CharField(max_length=32)
#     price = models.FloatField()
#     num = models.IntegerField()
#
#     class Meta:
#         db_table="detail"