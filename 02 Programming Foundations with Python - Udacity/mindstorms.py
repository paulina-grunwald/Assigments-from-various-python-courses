#this program will draw a circle by drawing multiple squeres
# https://docs.python.org/3.2/library/turtle.html#turtle.bgcolor

import turtle

def draw_square():
    #turtle.Screen() - class defines graphics windows as a playground for the drawing turtles.nes
    # graphics windows as a playground for the drawing turtles.
    window = turtle.Screen()
    #Set or return background color of the window
    window.bgcolor("red")

    #draw  a squere
    pen = turtle.Turtle()
    #select shape
    pen.shape("turtle")
    #select color
    pen.color("green")
    #select speed
    pen.speed("normal")
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
    pen.forward(100)

    #exit programme
    window.exitonclick()

draw_square()