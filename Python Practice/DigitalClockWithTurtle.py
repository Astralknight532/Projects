# -*- coding: utf-8 -*-
"""

this is a digital clock made using Turtle
"""

import time
import datetime as dt
import turtle

# a turtle to display time
t = turtle.Turtle()

# a turtle to create a recetangular box
t1 = turtle.Turtle()

# create a screen
s = turtle.Screen()

# set screen's background color
s.bgcolor('blue')

# obtain current hour, minute, & second from the system
sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour
t1.pensize(3)
t1.color('black')
t1.penup()

# set the turtle's position
t1.goto(-20, 0)
t1.pendown()

# create a rectangular box
for i in range(2):
    t1.forward(200)
    t1.left(90)
    t1.forward(70)
    t1.left(90)
    
# hide the turtle
t1.hideturtle()

while True:
    t.hideturtle()
    t.clear()
    
    # display the time
    t.write(str(hr).zfill(2) + ':' + str(min).zfill(2) + ':' + str(sec).zfill(2), font = ('Arial Narrow', 35, 'bold'))
    time.sleep(1)
    sec += 1
    
    if sec == 60:
        sec = 0
        min += 1
        
    if min == 60:
        min = 0
        hr += 1
        
    if hr == 23:
        hr = 0