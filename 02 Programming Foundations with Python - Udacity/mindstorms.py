#this program will draw a circle by drawing multiple squeres
# https://docs.python.org/3.2/library/turtle.html#turtle.bgcolor

import turtle

def draw_square(some_turtle):
    #remember that range will count from 1 to 4
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    #turtle.Screen() - class defines graphics windows as a playground for the drawing turtles.nes
    # graphics windows as a playground for the drawing turtles.
    window = turtle.Screen()
    #Set or return background color of the window
    window.bgcolor("red")

    #create first turtle Ben
    ben = turtle.Turtle()
    #select shape
    ben.shape("turtle")
    #select color
    ben.color("green")
    #select speed
    ben.speed("normal")
    #use function draw_square using ben turtle
    draw_square(ben)

    #create second turtle Josh
    josh = turtle.Turtle()
    josh.shape("arrow")
    josh.color("yellow")
    josh.speed("normal")
    josh.circle(100)
    #exit programme
    window.exitonclick()

draw_art()

