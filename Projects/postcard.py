import turtle
import math
turtle.speed(0)
turtle.color("red")
turtle.bgcolor("black")
turtle.pensize(2)

def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y


for i in range(1, 16):
    turtle.penup()
    x, y = corazon(0)
    turtle.goto(x * i,y * i)
    turtle.pendown()
    for n in range(0, 628, 5):
        x, y = corazon(n/100)
        turtle.goto(x*i, y*i)
    turtle.hideturtle()
turtle.penup()
turtle.goto(0, -340)
turtle.color("white")
turtle.write("I love you, my lovely wife", align="center", font=("ESTRANGELO EDESSA", 20, "bold"))
turtle.done()