import turtle

tim = turtle.Turtle()
tim.shape("turtle")

for x in range(4):
    tim.forward(100)
    tim.right(90)

tim.penup()
tim.forward(150)
tim.pendown()

for x in range(3):
    tim.forward(200)
    tim.left(120)



