import turtle
def drawCurve(turtle, L,n):

    if n== 0:
        turtle.forward(L)
    else :
        drawCurve(turtle,L/3,n-1)
        turtle.left(60)
        drawCurve(turtle,L/3,n-1)
        turtle.right(120)
        drawCurve(turtle,L/3,n-1)
        turtle.left(60)
        drawCurve(turtle,L/3,n-1)


turtle.setup(800,400)
drawCurve(turtle,300,1)
turtle.exitonclick()


