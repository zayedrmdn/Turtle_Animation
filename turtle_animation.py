from turtle import *
from random import randint

speed(0.1)
penup()
goto(-140, 140)

for j in range(15):
    write(j, align = 'center')
    right(90)

    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)

    penup()
    backward(160)
    left(90)
    forward(20)

plyr1 = Turtle()
plyr1.color('magenta')
plyr1.goto(-160, 100)
plyr1.pendown()

for turn in range(10):
    plyr1.right(36)

plyr2 = Turtle()
plyr2.color('red')
plyr2.shape('turtle')

plyr2.penup()
plyr2.goto(-160, 70)
plyr2.pendown()

plyr3 = Turtle()
plyr3.shape('turtle')
plyr3.color('light green')

plyr3.penup()
plyr3.goto(-160, 40)
plyr3.pendown()

for turn in range(60):
    plyr3.right(6)

plyr4 = Turtle()
plyr4.shape('turtle')
plyr4.color('blue')

plyr4.penup()
plyr4.goto(-160, 10)
plyr4.pendown()

for turn in range(30):
    plyr4.left(12)

for turn in range(100):
    plyr1.forward(randint(1, 5))
    plyr2.forward(randint(1, 5))
    plyr3.forward(randint(1, 5))
    plyr4.forward(randint(1, 5))