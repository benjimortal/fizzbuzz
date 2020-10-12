import turtle


wn = turtle.Screen()
wn.bgcolor("black")


def main():
    ball = turtle.Turtle()
    #wn.tracer(90)
    wn.title("stutsvägg")

    balls = []

    for i in range(10):
        balls.append(turtle.Turtle())

    for ball in balls:
        ball.shape("circle")
        ball.color("pink")
        ball.penup()
        ball.speed(0)
        ball.goto(0, 200)
        ball.dy = 0
        ball.dx = 2
    gravity = 0.1

    while True:
        wn.update()
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        if ball.ycor() < - 304:
            ball.dy *= -1
        if ball.ycor() > 304:
            ball.dy *= -1

        if ball.xcor() > 360:
            ball.dx *= -1
        if ball.xcor() < -360:
            ball.dx *= -1

    wn.mainloop()


if __name__ == '__main__':
    main()
