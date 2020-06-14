# 绘制三角形
# 避免反复调用命令forward和left
from turtle import *

# 方法一
for i in range(3):
    forward(100)
    left(120)

# 方法二：
circle(100, None, 3)