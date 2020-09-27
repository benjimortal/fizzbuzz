
"""Ant, simple animation demo.

Exercises

1. Wrap ant around screen boundaries.
2. Make the ant leave a trail.
3. Change the ant color based on position.
   Hint: colormode(255); color(0, 100, 200)

"""

from random import *
from turtle import *
from freegames import vector

ant = vector(0, 0)
aim = vector(2, 0)

def wrap(value):
    "Wrap value around -200 and 200."
   # if value < -200 or value > 200: #detta is satserna gör att bollen kommer tillbaka från andra sidan om den försvinner.
    #    return value * -1

    if not -200 < value < 200: # om value är mellan -200 och 200 så är myran på skärmen så keyword not gör att om den inte är i skärmen så gör dett.
        return True, value * -1


   #if value < -200: #detta is satserna gör att bollen kommer tillbaka från andra sidan om den försvinner.
        #return 200
    #if value > 200:
     #   return -200

    return False, value

def draw():
    "Move ant and draw screen."
    ant.move(aim)
    wrapped_x, ant.x = wrap(ant.x)
    wrapped_y, ant.y = wrap(ant.y)

    aim.move(random() - 0.5)
    aim.rotate(random() * 10 - 5)

    #clear()
    if not wrapped_x and not wrapped_y:
        pendown()
    r = int(abs(ant.x))
    g = int(abs(ant.y))
    b = (int(abs(ant.x)) * int(abs(ant.y))) % 255
    color(r,g,b)
    goto(ant.x, ant.y)
    up()
    pensize(50)
    #dot(10)

    if running:
        ontimer(draw, 50)

setup(420, 420, 370, 0)
colormode(255)
hideturtle()
tracer(False)
up()
running = True
draw()
done()



