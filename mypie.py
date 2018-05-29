import turtle
import math


def slices(t, exterior, interior, angle):
    t.fd(interior)
    t.rt(180-angle)
    t.fd(exterior)
    t.rt(180 - angle)
    t.fd(interior)


def pie(t, n, r):
    angle = 90 - 180 / n
    ext = (r * math.sin(math.radians(360/n))) / math.sin(math.radians(angle))
    for i in range(n):
        slices(t, ext, r, angle)
        t.rt(180)


bob = turtle.Turtle()

pie(bob, 7, 100)

turtle.mainloop()
