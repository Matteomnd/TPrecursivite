import turtle
from EXERCICE6_Partie2 import *
def drawFullCurve(turtle,L,n):
        drawCurve(turtle,L,n)
        turtle.right(120)
        drawCurve(turtle,L,n)
        turtle.right(120)
        drawCurve(turtle,L,n)


turtle.setup(800,400)
drawFullCurve(turtle,500,10)
turtle.exitonclick()
