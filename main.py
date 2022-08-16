# import turtle
import turtle
from turtle import *

# screen for output
screen = turtle.Screen()
# Defining a turtle Instance
t = turtle.Turtle()

speed(1)

# initially penup()
t.penup()
t.goto(-200, 125)
t.pendown()
# Orange Rectangle
# white rectangle

t.color("blue")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(84)
t.right(90)
t.forward(400)
t.end_fill()
t.left(90)
t.forward(84)

# Green Rectangle
t.color("green")
t.begin_fill()
t.forward(84)
t.left(90)
t.forward(400)
t.left(90)
t.forward(84)
t.end_fill()

# Big White Circle
t.penup()
t.goto(30, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()

# for stick of the flag
t.color("black")
t.pensize(10)
t.penup()
t.goto(-200, 125)
t.right(180)
t.pendown()
t.forward(800)

t.color("red")
t.pensize(5)
t.penup()
t.goto(-195, 42)
t.right(270)
t.pendown()
t.forward(395)

t.color("red")
t.pensize(5)
t.penup()
t.goto(-195, -44)
t.right(0)
t.pendown()
t.forward(392)

  
# giving title to our turtle graphics window
# w.title("Starry Sky")
  
# making function to draw the stars
def stars():
    for i in range(5):
        t.color("white")
        t.pensize(2)
        t.penup()
        t.goto(-100,100)
        t.right(144)
        t.pendown()
        t.forward(3) 

      
        t.color("white")
        t.pensize(2)
        t.penup()
        t.goto(-80,100)
        t.right(144)
        t.pendown()
        t.forward(3)

      
        t.color("white")
        t.pensize(2)
        t.penup()
        t.goto(-60,100)
        t.right(144)
        t.pendown()
        t.forward(3)
        # pastki qator
        t.color("white")
        t.pensize(2)
        t.penup()
        t.goto(-120,80)
        t.right(144)
        t.pendown()
        t.forward(3)

        t.color("white")
        t.pensize(2)
        t.penup()
        t.goto(-100,80)
        t.right(144)
        t.pendown()
        t.forward(3)
      
        t.color("white")
        t.pensize(2)
        t.penup()
        t.goto(-80,80)
        t.right(144)
        t.pendown()
        t.forward(3)
      
        t.color("white")
        t.pensize(2)
        t.penup()
        t.goto(-60,80)
        t.right(144)
        t.pendown()
        t.forward(3)
      #pastki qator
        t.color("white")
        t.pensize(2)
        t.penup()
        t.goto(-140,60)
        t.right(144)
        t.pendown()
        t.forward(3)

        t.color("white")
        t.pensize(2)
        t.penup()
        t.goto(-120,60)
        t.right(144)
        t.pendown()
        t.forward(3)

        t.color("white")
        t.pensize(2)
        t.penup()
        t.goto(-100,60)
        t.right(144)
        t.pendown()
        t.forward(3)

        t.color("white")
        t.pensize(2)
        t.penup()
        t.goto(-80,60)
        t.right(144)
        t.pendown()
        t.forward(3)

        t.color("white")
        t.pensize(2)
        t.penup()
        t.goto(-60,60)
        t.right(144)
        t.pendown()
        t.forward(3)
        
stars()
#Moon part 1
t.penup()
t.goto(-160, 67)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(20)
t.end_fill()

#Moon part 2
t.penup
t.goto(-150, 67)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(20)
t.end_fill()

turtle.done()
