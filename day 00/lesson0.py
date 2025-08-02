from turtle import *

#we want to paint house

#step 1: draw a square

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of a door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(70, 135)

color("purple")
begin_fill()
right(55)
forward(60)
right(60)
right(32.5)
forward(60)
right(90)
forward(60)
right(95)
forward(70)
end_fill()

penup()
goto(135, 135)

color("purple")
begin_fill()
left(90)
forward(60)
left(60)
left(32.5)
forward(60)
left(90)
forward(60)
left(95)
forward(70)
end_fill()





exitonclick()