from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from myadmin.models import Types, Goods, Users, Orders
from PIL import Image

import time, json, os


def typeindex(request):
    """
    浏览商品类别信息

    :param request:
    """
    # 执行数据查询, 并把结果放到模板中
    lst = Types.objects.extra(select={'_has': 'concat(path, id)'}).order_by('_has')
    # 遍历查询结果，为每个结果对象追加一个pname属性，目的用于缩进标题
    for ob in lst:
        ob.pname = '. . . ' * (ob.path.count(',') - 1)
        # print(list[0].__dict__)
    context = {"typeslist": lst}
    return render(request, 'myadmin/type/index.html', context)