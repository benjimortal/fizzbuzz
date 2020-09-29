import random
from turtle import *

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


def draw_pole(turtle):
    turtle.penup()
    turtle.goto(-250, -150)
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
    turtle.pensize(10)
    turtle.forward(142)
    turtle.setheading(RIGHT)
    turtle.forward(100)


def draw_rope(turtle):
    turtle.setheading(DOWN)
    turtle.pensize(5)
    turtle.pencolor("grey")
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
    turtle.pensize(5)
    turtle.forward(150)


def draw_right_arm(turtle):
    turtle.backward(80)
    turtle.setheading(245)
    turtle.forward(65)
    turtle.backward(65)


def draw_left_arm(turtle):
    turtle.setheading(295)
    turtle.forward(65)
    turtle.backward(65)
    turtle.setheading(DOWN)
    turtle.forward(80)


def draw_right_leg(turtle):
    turtle.setheading(245)
    turtle.forward(65)
    turtle.backward(65)


def draw_left_leg(turtle):
    turtle.setheading(295)
    turtle.forward(65)
    turtle.backward(65)
    turtle.setheading(UP)
    turtle.forward(100)


def main():
    hidden_turtle = Turtle()
    hidden_turtle.hideturtle()

    word_turtle = Turtle()
    word_turtle.pencolor("green")
    word_turtle.hideturtle()

    used_turtle = Turtle()
    used_turtle.pencolor("blue")
    used_turtle.hideturtle()
    used_turtle.penup()
    used_turtle.goto(-100, -250)
    functions = [draw_left_leg, draw_right_leg, draw_left_arm, draw_right_arm, draw_body, draw_head, draw_rope, draw_cross_bar, draw_bar, draw_pole]

    words = ["apple", "duplex", "banjo", "bookworm", "beekeeper"]
    word = random.choice(words)
    hidden_word = "_ " * len(word)

    word_turtle.penup()
    word_turtle.goto(-100, -300)
    word_turtle.clear()
    word_turtle.write(hidden_word, font=("Arial", 20, "bold"))


    screen_tutrtle = Turtle()
    screen_tutrtle.hideturtle()
    screen = screen_tutrtle.getscreen()


    lives = 10
    used_letters = ""

    while lives > 0:
        used_turtle.clear()
        used_turtle.write("You have used letters: " + used_letters, font=("Arial", 16, "bold"))


        guessed_letter = ""
        while  len(guessed_letter) != 1 or not guessed_letter.isalpha():
            guessed_letter = screen.textinput("Enter a leter", "Letter")
            #guessed_letter = input("Enter a letter: ")
            used_letters += guessed_letter + " "

        new_hidden = ""
        lose_life = True
        for i, character in enumerate(word):
            if guessed_letter.lower() == character:
                new_hidden += character + " "
                lose_life = False
            else:
                new_hidden += hidden_word[i*2] + " "

        if lose_life:
            lives = lives - 1
            functions[lives](hidden_turtle) # vi gör en funktion stället att använda if och elif
            """if lives == 9:
                draw_pole(hidden_turtle)
            elif lives == 8:
                draw_bar(hidden_turtle)
            elif lives == 7:
                draw_cross_bar(hidden_turtle)
            elif lives == 6:
                draw_rope(hidden_turtle)
            elif lives == 5:
                draw_head(hidden_turtle)
            elif lives == 4:
                draw_body(hidden_turtle)
            elif lives == 3:
                draw_right_arm(hidden_turtle)
            elif lives == 2:
                draw_left_arm(hidden_turtle)
            elif lives == 1:
                draw_right_leg(hidden_turtle)
            elif lives == 0:
                draw_left_leg(hidden_turtle)"""

        hidden_word = new_hidden
        word_turtle.clear()
        word_turtle.write(hidden_word, font=("Arial", 20, "bold"))
        print("Lives:", lives)

        if "_" not in hidden_word:
            used_turtle.clear()
            used_turtle.write("You did it!!! :)", font=("Arial", 16, "bold"))
            break

    if "_" in hidden_word:
        used_turtle.clear()
        used_turtle.write("You are dead!!! :(", font=("Arial", 16, "bold"))
        word_turtle.clear()
        word_turtle.write("The word was:" + word, font=("Arial", 16, "bold"))
    done()


if __name__ == '__main__':
    main()
