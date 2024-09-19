from turtle import *
                           #Burning the first house
speed(15)
width(7)
color("red")    #shignita gulis gaferadeba da kvadretis gaketebaa 21 mde
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)          
end_fill()
#end of square

#drawing adoor

forward(70)
color("black")
begin_fill()
left(90)
forward(120)  #height of the door  #karebis gaketeba da ferebit amovseba end_fill amde
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color('black')    #make a roof and panting it   #saxurvais gaketeba da gulis gaferadeba
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(130, 130)                    # mausis ageba  da dadeba,goto ari kordinati
pendown()


color("cyan")    #window 1 start
begin_fill()
right(150)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()        #window 2 #finish

penup()
goto(50, 50)
pendown()


right(70)
penup()
goto(70, 130)
pendown()

color("cyan")      #window 2 start
begin_fill()
left(70)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()        #window 2 finish

penup()
goto(200, 200)
pendown()


left(210)                            #saxlis gareta kantebis gaketeba 112 mde 
forward(200)
right(240)
forward(200)
left(120)
forward(200)


right(90)
forward(200)

right(90)
forward(200)

right(90)
forward(200)


right(90)
forward(200)

color("yellow")               # fanjrebis kantebis gaketeba
begin_fill()
end_fill()


penup()
goto( 70, 130)
pendown()


width(7)
left(90)     
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

penup()
goto(130, 130)
pendown()

left(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

right(90)
forward(50)

penup()
goto(300, 5)
pendown()

color("brown")        #  xis gaketeba      
right(90)
begin_fill()
forward(250)
right(90)
forward(50)
right(90)
forward(250)
right(90)
forward(50)
end_fill()

penup()
goto(300, 250)
pendown()

color("green")
forward(100)
begin_fill()
right(90)
forward(90)
right(90)
forward(250)
right(90)
forward(90)
right(90)
forward(147)
end_fill()

penup()
goto(-200, 5)
pendown()

color("brown")           
right(90)
begin_fill()
forward(250)
right(90)
forward(50)
right(90)
forward(250)
right(90)
forward(50)
end_fill()

penup()
goto(-200, 250)
pendown()

color("green")
forward(100)
begin_fill()
right(90)
forward(90)
right(90)
forward(250)
right(90)
forward(90)
right(90)
forward(147)
end_fill()           #xis gaketebis damtavreba

penup()            #trasis gaketebis dawyeba 
goto(-350, -50)
pendown()

color("black")
right(180)
begin_fill()
forward(800)
end_fill()

penup()
goto(-350, -150)
pendown()

color("black")
begin_fill()
forward(800)
end_fill()

penup()
goto(-350, -100)
pendown()

color("red")
begin_fill()
forward(100)

penup()
goto(-170, -100)
pendown()

color("red")
begin_fill()
forward(100)

penup()
goto(10, -100)
pendown()

color("red")
begin_fill()
forward(100)

penup()
goto(200, -100)
pendown()

color("red")
begin_fill()
forward(100)

penup()
goto(370, -100)
pendown()

color("red")
begin_fill()
forward(80)


penup()
goto(-500, 400)
pendown()


color("yellow")      #mzis gaketebis dawyeba
circle(45)
begin_fill()
forward(10)        
end_fill()
   
    
    
    
    
    
    
    
    
    
    
    
                        #Completion of the first house
exitonclick()