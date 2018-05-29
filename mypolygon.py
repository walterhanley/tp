import turtle
import math


def square(turt, length):
    """
    Draws a square with the given side length. turt is a turtle.
    """
    for i in range(4):
        turt.fd(length)
        turt.lt(90)
    turtle.mainloop()


def polygon(turt, length, n):
    """
    Draws n-sided polygon with the given side length. turt is a turtle.
    """
    for i in range(n):
        turt.fd(length)
        turt.lt(360/n)
    turtle.mainloop()


def circle(turt, r):
    """
    Draws a circle with radius r. turt is a turtle.
    """
    n = 360
    length = (2 * math.pi * r) / n
    polygon(turt, length, n)


def arc(turt, r, angle):
    """
    Draws an angle-length arc with radius r. turt is a turtle.
    """
    length = (2 * math.pi * r) / 360
    for i in range(angle):
        turt.fd(length)
        turt.lt(1)
    turtle.mainloop()


bob = turtle.Turtle()
arc(bob, 200, 270)
