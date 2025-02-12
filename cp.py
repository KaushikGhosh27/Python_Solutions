import turtle
import math
import colorsys
phi = 180 * (3 - math.sqrt(5))
t = turtle.Pen()
t.speed(0)
def square(t, size):
    for tmp in range(0,4):
        t.forward(size)
        t.right(90)
num = 200
for x in reversed(range(0, num)):
    t.fillcolor(colorsys.hsv_to_rgb(x/num, 1.0, 1.0))
    t.begin_fill()
    t.circle(5 + x, None, 11)
    square(t, 5 + x)
    t.end_fill()
    t.right(phi)
    t.right(.8)
turtle.mainloop()
