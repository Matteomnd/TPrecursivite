import turtle
def drawCurve(turtle, I):
    if I==0:
        turtle.forward(I)
    else :
        drawCurve(turtle,I/4)
        turtle.left(60)
        drawCurve(turtle,I/4)
        turtle.right(120)
        drawCurve(turtle,I/4)
        turtle.left(60)
        drawCurve(turtle,I/4)


turtle.setup(800,400)
drawCurve(turtle, 300)
turle.exitonclick()







