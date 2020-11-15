from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from myadmin.models import Users
from PIL import Image, ImageDraw, ImageFont

import hashlib
import random
import io


# Create your views here.
def index(request):
    """
    进入后台管理首页

    :param request:
    """
    return render(request, 'myadmin/index.html')


def users(request, pIndex=1):
    """
    执行分页操作

    :param request:
    :param pIndex:
    """
    print(pIndex)
    print('*' * 30)
    # 获取会员信息
    lst = Users.objects.filter()

    # 判断并封装搜索条件
    # 定义一个用于维持搜索条件的变量
    where = []
    # 为什么不直接用GET['name']?
    # request.POST或request.GET都是QueryDict对象的实例
    # 直接GET['name']不安全,在Get数据时 name不可得,可能引发KeyError
    # 这里的get()是python的字典数据类型内置方法,
    # 使用get(‘name’, ‘’) 提供一个缺省的返回值’’ (一个空字符串)
    if request.GET.get('name', '') != '':
        lst = lst.filter(name__contains=request.GET.get('name'))
        where.append('name=' + request.GET.get('name'))
    if request.GET.get('sex', '') != '':
        lst = lst.filter(sex=request.GET.get('sex'))
        where.append('sex=' + request.GET.get('sex'))
    print('-------------')
    print(pIndex)
    # 传入数据和页大小来创建分页对象
    p = Paginator(lst, 4)

    # 判断页号没有值时初始化为1
    if pIndex == '':
        pIndex = '1'

    pIndex = int(pIndex)
    print(pIndex)
    list2 = p.page(pIndex)  # 获取当前页数据
    plist = p.page_range  # 获取页码信息
    # 封装分页信息
    context = {
        'userslist': list2,
        'plist': plist,
        'pIndex': pIndex,
        'where': where
    }
    return render(request, 'myadmin/users/index.html', context)


def usersindex(request):
    """
    浏览会员

    :param request:
    """
    # 执行数据查询,并放入到模板中
    lst = Users.objects.all()
    context = {'userslist': lst}
    return render(request, 'myadmin/users/index.html', context)


def usersadd(request):
    """
    进入添加会员信息页面

    :param request:
    """
    return render(request, 'myadmin/users/add.html')


def usersinsert(request):
    """
    添加会员信息

    :param request:
    """
    try:
        ob = Users()
        ob.username = request.POST['username']
        ob.name = request.POST['name']
        # 获取密码, 用md5加密
        m = hashlib.md5()
        m.update(bytes(request.POST['password'], encoding='utf8'))
        ob.password = m.hexdigest()
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = 1
        ob.save()
        context = {'info': '修改成功! '}
    except:
        context = {'info': '修改失败! '}
    return render(request, 'myadmin/info.html', context)


def usersdel(request, uid):
    """
    删除会员信息

    :param request:
    :param uid:
    """
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功'}
    except:
        context = {'info': '删除失败'}
    return render(request, 'myadmin/info.html', context)


def usersedit(request, uid):
    """
    打开会员信息编辑表单

    :param request:
    :param uid:
    """
    try:
        ob = Users.objects.get(id=uid)
        context = {'user': ob}
        return render(request, 'myadmin/users/edit.html', context)
    except:
        context = {'info': '没有找到要修改的信息'}
    return render(request, 'myadmin/info.html', context)


def usersupdate(request, uid):
    """
    修改会员信息

    :param request:
    :param uid:
    """
    try:
        ob = Users.objects.get(id=uid)

        ob.name = request.POST['name']
        ob.sex = request.POST['sex']
        ob.code = request.POST['code']
        ob.address = request.POST['address']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = request.POST['state']
        ob.save()

        context = {'info': '修改成功! '}
    except:
        context = {'info': '修改失败! '}
    return render(request, 'myadmin/info.html', context)


def login(request):
    """
    管理员登录表单

    :param request:
    """
    return render(request, 'myadmin/login.html')


def dologin(request):
    """
    登录管理员

    :param request:
    """
    # 校验验证码
    verification_code = request.session['verification_code']
    code = request.POST['code'].lower()
    if verification_code != code:
        context = {'info': '验证码错误! '}
        return render(request, 'myadmin/login.html', context)

    try:
        # 根据账号名获取登录者信息
        user = Users.objects.get(username=request.POST['username'])
        # 判断当前用户是否是后台管理员用户
        if user.state == 0:
            # 验证密码
            m = hashlib.md5()
            m.update(bytes(request.POST['password'], encoding='utf8'))
            if user.password == m.hexdigest():
                # 登录成功, 将登录信息放入session中, 并跳转页面
                request.session['adminuser'] = user.name
                return redirect(reverse('myadmin_index'))
            else:
                context = {'info': '登录密码错误! '}
        else:
            context = {'info': '此用户非后台管理员用户 '}
    except:
        context = {'info': '登录账号错误! '}

    return render(request, 'myadmin/login.html', context)


def logout(request):
    """退出管理员"""
    # 清除登录的session信息
    del request.session['adminuser']
    # 跳转到管理员登录页面
    return redirect(reverse('myadmin_login'))


def verify(request):
    """"登录验证码"""
    # 定义变量,图片的背景色,宽,高
    bgcolor = (150, 154, 194)
    width = 100
    height = 25
    # 创建图片对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建笔画对象
    draw = ImageDraw.Draw(im)

    # 调用笔画的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill)

    # 定义验证码备选值
    str1 = 'ABCD23EFGHJK456MNOPQRS789TUVMXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象, ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('static/admin/font/STXIHEI.TTF', 21)
    # 构造字体颜色
    for i in range(0, 4):
        fontcolor = (
            random.randrange(0, 255),
            random.randrange(0, 255),
            random.randrange(0, 255)
        )
        draw.text((5 + i * 24, -4), rand_str[i], fill=fontcolor, font=font)
    # 释放画笔
    del draw
    # 存入session, 用于进一步验证
    request.session['verification_code'] = rand_str.lower()
    # 内存文件操作
    buf = io.BytesIO()
    # 就图片保存在内存中,文件类型.png
    im.save(buf, 'png')
    # 就内存中的图片数据返回给客户端, MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')