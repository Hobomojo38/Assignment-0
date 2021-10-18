# Course: ITI1120
# Assignment 0
# Zimmermann, Max
# 0300249929

import turtle
s=turtle.Screen()
t=turtle.Turtle(shape='turtle')

t.penup()
t.goto(-300,0)
t.pendown()

# your code should go right after this line

for i in range(7):
    t.setheading(-45)
    t.circle(50,90)


t.penup()
t.goto(-100,200)
t.pendown()
t.circle(50)
t.penup()

#To keep the window active

while True:
    t.goto(0,-50)