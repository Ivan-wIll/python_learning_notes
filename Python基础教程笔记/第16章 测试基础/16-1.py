# 简单的测试程序
# 假设你要编写一个模块，其中只包含一个根据矩形的宽度和高度计算面积的函数。
# 动手编写代码前，编写一个单元测试，其中包含一些你知道答案的例子
from area import rect_area
height = 3
width = 4
correct_answer = 12
answer = rect_area(height, width)
if answer == correct_answer:
    print('Test passed ')
else:
    print('Test failed ')
