import random
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
    hidden_turtle = Turtle()
    #hidden_turtle.hidenturtle()
    word_turtle = Turtle()
    function = [draw_left_leg, draw_right_leg, draw_left_arm, draw_right_arm, draw_body, draw_head, draw_cross_bar, draw_bar, draw_rope]
    words = ["apple", "duplex", "banjo", "bookworm", "beekeeper"]
    word = random.choice(words)
    hidden_word = "_ " * len(word)
    print(hidden_word)
    lives = 10
    used_letters = ""

    while lives > 0:
        print("You have used the letters:", used_letters)
        guessed_letter = input("Enter a letter: ")
        used_letters += guessed_letter + " "

        new_hidden = ""
        lose_life = True
        for i, character in enumerate(word):
            if guessed_letter.lower() == character:
                new_hidden += character + " "
                lose_life = False
            else:
                new_hidden += hidden_word[i * 2] + " "

        if lose_life:
            lives = lives - 1
            if lives == 9:
                draw_pole(hidden_turtle)
            elif lives == 8:
                draw_bar(hidden_turtle)
            elif lives == 7:
                draw_cross_bar(hidden_turtle)

        hidden_word = new_hidden
        print(hidden_word)
        print("Lives:", lives)

        if "_" not in hidden_word:
            print("You did it!!!")
            break
    done()


if __name__ == '__main__':
    main()
