import turtle
import math


def triangle(t, ph):
    hypo = math.sqrt(ph**2 + 100**2)
    ext_ang = 180 - math.degrees(math.acos(100/hypo))
    t.fd(ph)
    t.lt(90)
    t.fd(100)
    t.lt(ext_ang)
    t.fd(hypo)
    t.lt(180)
    return hypo


def spiral(t, n):
    hypo = triangle(t, 100)
    for i in range(n-1):
        hypo = triangle(t, hypo)


bob = turtle.Turtle()

spiral(bob, 16)

turtle.mainloop()
