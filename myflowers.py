import turtle

from polygon import arc


def petal(t, r, angle):
    '''
    Draws a petal shape made out of two arcs with radius r and given angle.
    '''
    for i in range(2):
        arc(t, r, angle)
        # Subtracting 180 from the angle of the arc makes sure we end at start.
        t.lt(180-angle)


def flower(t, r, angle, n):
    '''
    Draws an n-petaled flower by iterating over range.
    '''
    for i in range(1):
        petal(t, r, angle)
        # Rotates turtle so there's one petal in every chunk of the circle.
        t.lt(360/n)


bob = turtle.Turtle()

flower(bob, 100, 45, 7)

turtle.mainloop()
