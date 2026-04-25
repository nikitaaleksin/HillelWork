import turtle
import math
turtle.speed(0)
turtle.color("red")
turtle.bgcolor("black")
turtle.pensize(2)
turtle.setup(width=800, height=800)

def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y
for i in range(1, 16):
    turtle.penup()



    angle = i * 0.1


    for n in range(0, 629, 5):
        x_raw, y_raw = corazon(n / 100)


        x_scaled = x_raw * i
        y_scaled = y_raw * i


        x = x_scaled * math.cos(angle) - y_scaled * math.sin(angle)
        y = x_scaled * math.sin(angle) + y_scaled * math.cos(angle)

        turtle.goto(x, y)
        turtle.pendown()

    turtle.hideturtle()