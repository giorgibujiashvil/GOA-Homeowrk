my_name = "giorgi"
my_surname ="bujiashvili"
my_age = 15
my_age10yearsago ="10 wlis shemdeg viqnebi 25lwis"
print(my_name+ " "+my_surname+" "+my_age+" "+my_age10yearsago)

from turtle import *

#სახლი0


width(7)
speed(1000)

color("red")
begin_fill()
forward (200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square()

forward(70)
color("green")
left(90)
begin_fill()
forward (120) 
right(90)
forward(60)
right(90)
forward(120)

end_fill()


penup()
goto(200, 200)
pendown()

color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()
left(30)

forward(30)
left(90)
forward(20)
pendown()
begin_fill()
forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
end_fill()
penup()


#ფანჯარა

right(90)
forward(130)
pendown()
begin_fill()
forward (35)
right(90)

forward(35)
right(90)

forward(35)
right(90)

forward(35)
end_fill()

penup()
goto(x=200,y=0)
pendown()

#სახლი 1

color("brown")
begin_fill()
right(90)
forward(200)


left(90)
forward(200)

left(90)
forward(200)
end_fill()

color("blue")
begin_fill()
right(120)
forward(200)

right(120)
forward(200)

left(60)
end_fill()
penup()
goto(x=230, y=170)
pendown()

begin_fill()
forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)
forward(40)
right(90)
end_fill()

penup()
forward(100)
pendown()

begin_fill()
forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)
end_fill()

penup()
goto(x=280,y=0)
pendown()

color("yellow")
begin_fill()
left(90)
forward(100)
right(90)
forward(50)

right(90)
forward(100)
end_fill()



#სახლი2

penup()
goto(x=0,y=0)
pendown()
color("purple")
right(90)
forward(200)



right(90)
forward(200)

color("blue")
begin_fill()
right(90)
forward(200)

left(120)
forward(200)
end_fill()

left(120)
forward(200)
left(30)
penup()
goto(x=-40,y=170)
pendown()
forward(40)

end_fill()



begin_fill()

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

end_fill()

penup()
backward(140)
pendown()


begin_fill()
forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)

forward(40)
right(90)
end_fill()
penup()
goto(x=-140,y=0)
pendown()
color("black")
begin_fill()
left(90)
forward(100)

right(90)
forward(50)
right(90)
forward(100)
end_fill()


speed(100)
color("darkgreen")
begin_fill()
left(90)
forward(3000)
right(90)
forward(2000)
right(90)
forward(5000)
right(90)
forward(2000)
right(90)
forward(7000)
end_fill()
color("brown")
penup()









penup()
goto(x=-1000,y=400)
pendown()
color("green")
begin_fill()
forward(5000)
left(90)
forward(200)
left(90)
forward(5000)
left(90)
forward(200)
end_fill()


penup()
goto(x=-600,y=300)
pendown()
color("yellow")

begin_fill()
circle(40)
end_fill()

right(90)
forward(30)
backward(140)

forward(70)
left(90)

forward(70)
backward(140)
forward(70)
left(45)
forward(70)
backward(140)
forward(70)
right(90)
forward(70)
backward(140)


















exitonclick()