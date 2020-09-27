from turtle import *

def main():

    hideturtle()
    hangman_turtle = Turtle()
    hangman_turtle.pensize(10)
    hangman_turtle.left(90)
    hangman_turtle.forward(200)

    input_turtle = Turtle()
    screen = input_turtle.getscreen()
    letter = screen.textinput("Enter the guessed letter: ", "Letter :")

    write_turtle = Turtle()
    write_turtle.hideturtle()
    write_turtle.pencolor("red")

    write_turtle.penup()
    write_turtle.goto(-200, -200)
    write_turtle.pendown()
    write_turtle.write(f"_ _ _ {letter.upper()} _ _ T", font=("Arial", 15, "normal"))








    done()

if __name__ == '__main__':
    main()
