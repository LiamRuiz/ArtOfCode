import turtle
from random import *


bob = turtle.Turtle()
turtle.colormode(255)


def tree (x,y):
    jump(x,y)
    polygon(3,100,"green")
    bob.forward(40)
    bob.right(90)
    polygon(4,25,"brown")
    bob.left(90)

    
def polygon (size, side, c):
    bob.color( c )
    bob.begin_fill()
    angle = 360 / side
    for times in range(side):
        bob.forward (size)
        bob.left (angle)
    bob.end_fill()

    
def jump (x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def comet (size,angle,length):

    for times in range(length):
        bob.forward(size)
        bob.left(angle)
        bob.width(times)


def stair(distance, amount, c, w):
    bob.color(c)
    bob.width(w)
    for times in range( amount ):
        bob.forward( distance )
        bob.left( 90 )
        bob.forward( distance )
        bob.right( 90 )


def DrawSquare(sizeS, sizeC ):
    bob.width(5)
    for times in range(4):
        bob.forward(sizeS)
        bob.left( 90 )
        bob.circle(sizeC)

def Flower(size,c):

    for times in range(10):
        polygon(8,10,"pink")
        bob.left(50)

        bob.color("green")
        bob.width(5)
        bob.forward(300)

def angleL(times):

    for times in range(10):
        bob.forward(5)
        bob.left(10)

def angleR(times):

    for times in range(10):
        bob.forward(5)
        bob.right(10)
