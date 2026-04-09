import turtle
import time
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Heart Animation")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# رسم قلب
def draw_heart(size, color):
    t.color(color)
    t.begin_fill()
    t.left(140)
    t.forward(size)

    for _ in range(200):
        t.right(1)
        t.forward(size * 0.017)

    t.left(120)

    for _ in range(200):
        t.right(1)
        t.forward(size * 0.017)

    t.forward(size)
    t.end_fill()
    t.setheading(0)

# رسم الأشعة
def draw_rays(length):
    t.penup()
    t.goto(0, 0)
    t.color("#ff4d4d")

    for angle in range(0, 360, 10):
        t.setheading(angle)
        t.pendown()
        t.forward(length)
        t.penup()
        t.goto(0, 0)

# كتابة الاسم مع حركة
def moving_text():
    text = turtle.Turtle()
    text.hideturtle()
    text.color("white")
    text.penup()

    for y in range(-150, -50, 2):
        text.clear()
        text.goto(0, y)
        text.write("Hassan", align="center", font=("Arial", 26, "bold"))
        time.sleep(0.03)

# 💓 حركة النبض
colors = ["#330000", "#660000", "#990000", "#cc0000", "#ff1a1a", "#ff4d4d"]

for i in range(5):
    for size in range(180, 210, 5):
        t.clear()
        draw_heart(size, colors[i % len(colors)])
        draw_rays(size)
        time.sleep(0.05)

    for size in range(210, 180, -5):
        t.clear()
        draw_heart(size, colors[i % len(colors)])
        draw_rays(size)
        time.sleep(0.05)

# كتابة الاسم
moving_text()

turtle.done()
