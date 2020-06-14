# 绘制八边形
import turtle

# 方法一：
for i in range(8):
    turtle.forward(100)
    turtle.left(45)

# 方法二：
turtle.circle(100, None, 8)