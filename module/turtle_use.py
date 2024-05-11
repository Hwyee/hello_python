# 画图
import time
import turtle

t = turtle.Turtle()
t.shape("turtle")


t.write("Hello, World!", font=("Arial", 20, "normal"))


for i in range(4):
    t.forward(100)
    t.left(30)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(150)
    t.forward(100)
    t.left(180)
time.sleep(30)
