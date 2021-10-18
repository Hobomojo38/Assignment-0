# Course: ITI1120
# Assignment 0
# Zimmermann, Max
# 0300249929

import turtle
s=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()

# Place your code after this line

def Circle(num):
    t2.sety(-num)
    t2.circle(num)

t1.penup()
t2.penup()

#Draw axies

t1.setpos(-400,0)
t1.pendown()
t1.setpos(400,0)
t1.penup()

t2.setpos(0,400)
t2.pendown()

#Draw Circles while drawing send half of y-axis

for i in [20, 100, 150, 200]:
    Circle(i)

t2.sety(-400)
t2.penup()

# Diagonal Axies

t2.setpos(-300,-300)
t2.pendown()
t2.setpos(300,300)
t2.penup()

t1.setpos(300,-300)
t1.pendown()
t1.setpos(-300,300)
t1.penup()

t1.setheading(135)
t2.setheading(45)

#To keep the window active

while True:
    t1.setpos(-300,300)