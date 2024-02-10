import turtle
from turtle import Turtle, Screen
import random

# import colorgram

tim = Turtle()
tim.shape("turtle")
tim.color("deeppink4")
tim.pensize(2)
turtle.colormode(255)
tim.speed("fastest")


# colors = colorgram.extract("image.jpg", 50)


def draw_spirograph(size_of_gap, color_list):
    for i in range(int(360 / size_of_gap)):
        tim.color(random.choice(color_list))
        tim.circle(10)
        tim.left(size_of_gap)


def draw_filled_circle(color_list):
    r = 10
    col = random.choice(color_list)
    tim.fillcolor(col)
    tim.begin_fill()
    tim.circle(r)
    tim.end_fill()


def draw_a_row():
    for _ in range(10):
        draw_filled_circle(corrected_colors)
        tim.up()
        tim.forward(30)
    tim.left(90)
    tim.forward(30)
    tim.left(90)
    tim.forward(300)
    tim.left(180)


'''
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb
'''
'''
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
'''
corrected_colors = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
                    (122, 175, 156), (226, 198, 131), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126),
                    (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35),
                    (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171),
                    (177, 204, 185), (49, 62, 84), (164, 203, 208), (183, 190, 204), (83, 70, 40), (11, 112, 106)]

for _ in range(10):
    draw_a_row()

screen = Screen()
screen.exitonclick()
