from turtle import *

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


def draw_pole(turtle):
    turtle.penup()
    turtle.goto(-200, -300)
    turtle.setheading(UP)
    turtle.pensize(30)
    turtle.pencolor("brown")
    turtle.pendown()
    turtle.forward(400)


def draw_bar(turtle):
    turtle.setheading(RIGHT)
    turtle.forward(200)


def draw_cross_bar(turtle):
    turtle.backward(200)
    turtle.setheading(UP)
    turtle.backward(100)
    turtle.setheading(45)
    turtle.pensize(20)
    turtle.forward(141)
    turtle.setheading(RIGHT)
    turtle.forward(100)


def draw_rope(turtle):
    turtle.setheading(DOWN)
    turtle.pensize(10)
    turtle.pencolor("chocolate2")
    turtle.forward(100)


def draw_head(turtle):
    turtle.setheading(LEFT)
    turtle.pensize(1)
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()


def draw_body(turtle):
    turtle.setheading(DOWN)
    turtle.pensize(2)
    turtle.forward(160)


def draw_right_arm(turtle):
    turtle.backward(80)
    turtle.setheading(225)
    turtle.forward(100)
    turtle.backward(100)


def draw_left_arm(turtle):
    turtle.setheading(315)
    turtle.forward(100)
    turtle.backward(100)


def draw_right_leg(turtle):
    turtle.setheading(DOWN)
    turtle.forward(80)
    turtle.setheading(225)
    turtle.forward(100)
    turtle.backward(100)


def draw_left_leg(turtle):
    turtle.setheading(315)
    turtle.forward(100)
    turtle.backward(100)


def main():
    hangman_turtle = Turtle()
    draw_pole(hangman_turtle)
    draw_bar(hangman_turtle)
    draw_cross_bar(hangman_turtle)
    draw_rope(hangman_turtle)
    draw_head(hangman_turtle)
    draw_body(hangman_turtle)
    draw_right_arm(hangman_turtle)
    draw_left_arm(hangman_turtle)
    draw_right_leg(hangman_turtle)
    draw_left_leg(hangman_turtle)

    done()

if __name__ == '__main__':
    main()