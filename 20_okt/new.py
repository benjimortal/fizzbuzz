#bouncing balls
import turtle
import random

wn = turtle.Screen()
wn.bgcolor("white")
wn.title("ball simulator")
wn.tracer(0)

balls = []

for _ in range(10):
    balls.append(turtle.Turtle())


for ball in balls:
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    ball.speed(1)
    x = random.randint(-290,290)
    y = random.randint(-290,290)
    ball.goto(x, y)
    ball.dy = (random.randint(-3, 3))/5+.1
    ball.dx = (random.randint(-3, 3))/5+.1

def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10

def move():
    pass


while True:
    wn.update()
    for ball in balls:
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)


    #check for a bounce
        if is_collided_with(ball, ball):
            ball.dy *=-1
            ball.dx *=-1
        if ball.ycor() <-300:
            ball.dy *=-1
        if ball.ycor() >+300:
            ball.dy *=-1
        if ball.xcor() >+300:
            ball.dx *=-1
        if ball.xcor() <-300:
            ball.dx *=-1


wn.mainloop()
