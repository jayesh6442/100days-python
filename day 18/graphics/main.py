print("welcome to python graphics")
from turtle import Turtle, Screen

timmy_the_turtle= Turtle()




timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.clone()
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(200)
timmy_the_turtle.left(45)
timmy_the_turtle.forward(899)



for _ in   range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()


































screen = Screen()
screen.exitonclick()