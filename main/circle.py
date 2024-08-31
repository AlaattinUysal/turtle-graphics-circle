from turtle import Turtle,Screen
from turtle import colormode
import random
tim = Turtle()

t = colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


tim.speed("fastest")

def draw_spirograph(size):
    for i in range(int(360 / size)):
        tim.pencolor(random_color())
        tim.circle(60)
        tim.setheading(tim.heading() + size)

draw_spirograph(10)


screen = Screen()
screen.exitonclick()
