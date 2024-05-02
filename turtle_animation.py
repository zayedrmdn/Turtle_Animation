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
plyr1.shape('turtle')

plyr1.penup()
plyr1.goto(-160, 100)
plyr1.pendown()



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



plyr4 = Turtle()
plyr4.shape('turtle')
plyr4.color('blue')

plyr4.penup()
plyr4.goto(-160, 10)
plyr4.pendown()



randomInt1 = randint(1, 5)
randomInt2 = randint(1, 5)
randomInt3 = randint(1, 5)
randomInt4 = randint(1, 5)

distance1 = 0;
distance2 = 0;
distance3 = 0;
distance4 = 0;

for i in range(100):
    distance1 += randint(1, 5)
    distance2 += randint(1, 5)
    distance3 += randint(1, 5)
    distance4 += randint(1, 5)

for turn in range(100):
    plyr1.forward(randomInt1)
    plyr2.forward(randomInt2)
    plyr3.forward(randomInt3)
    plyr4.forward(randomInt4)

minimum_distance = max(distance1, distance2, distance3, distance4)

if distance1 == minimum_distance:
    winner = "Player 1 (Magenta) Wins !!!"
elif distance2 == minimum_distance:
    winner = "Player 2 (Red) Wins !!!"
elif distance3 == minimum_distance:
    winner = "Player 3 (Light Green) Wins !!!"
else:
    winner = "Player 4 (Blue) Wins !!!"

plyr1.clear
plyr2.clear
plyr3.clear
plyr4.clear

plyr5 = Turtle()
plyr5.write(winner, True, align="center", font=("Arial", 40, "normal"))

input("Hit enter.")