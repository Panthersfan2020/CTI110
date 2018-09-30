import turtle

mypen = turtle.Turtle()
mypen.shape("turtle")


mypen.color("blue")

mypen.left(90)

for i in range(0,6):
    mypen.forward(100)
    mypen.forward(-40)
    mypen.left(40)
    mypen.forward(30)
    mypen.forward(-30)
    mypen.right(80)
    mypen.forward(30)
    mypen.forward(-30)
    mypen.left(40)
    mypen.forward(-60)

    mypen.right(60)


