from MyFunctions import *
turtle.bgcolor("black")

turtle.tracer(False)



for times in range(5000):
    x = randint(-700,700)
    y = randint(-700,700)
    size = randint(1, 3)
    side = randint(3,8)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    c = (r,g,b)

    jump(x, y)
    polygon(size,3,"yellow")

    
jump(0,0)
bob.color("cyan")
bob.begin_fill()
bob.circle(95)
bob.end_fill()
jump(10,130)
bob.color("white")

bob.begin_fill()
bob.left(90)
bob.forward(60)
bob.left(180)
bob.forward(60)
bob.left(45)
bob.forward(80)
bob.left(145)
bob.forward(80)
bob.left(45)
bob.forward(65)
bob.end_fill()


jump(40,150)
bob.color("black")


bob.begin_fill()
bob.circle(2)
bob.end_fill()


jump(-20,15)
bob.color("cyan")



bob.begin_fill()
bob.left(5)
bob.forward(150)
bob.left(105)
bob.forward(200)
bob.left(170)
bob.forward(175)
bob.right(90)
bob.forward(100)
bob.end_fill()

jump(0,35)

bob.begin_fill()
bob.right(5)
bob.forward(150)
bob.right(105)
bob.forward(200)
bob.right(170)
bob.forward(175)
bob.left(90)
bob.forward(100)
bob.end_fill()



jump(10,190)
bob.color("cyan")
bob.right(45)

bob.begin_fill()
for times in range(20):
    bob.forward(10)
    bob.right(1)

bob.left(90)

for times in range(20):
    bob.forward(10)
    bob.left(2)

bob.right(180)
for times in range(20):
    bob.forward(10)
    bob.right(1)

for times in range(20):
    bob.forward(10)
    bob.right(1)

bob.right(155)

bob.forward(170)

bob.left(70)
bob.forward(220)
bob.end_fill()



jump(-400,-200)
bob.color("gray")

bob.begin_fill()
bob.circle(95)
bob.end_fill()
jump(-280,-200)
bob.color("white")

bob.begin_fill()
bob.left(90)
bob.forward(60)
bob.left(180)
bob.forward(60)
bob.left(45)
bob.forward(80)
bob.left(145)
bob.forward(80)
bob.left(45)
bob.forward(65)
bob.end_fill()


jump(-240,-205)

bob.begin_fill()
bob.color("black")
bob.circle(3)
bob.end_fill()

bob.color("gray")
jump(-350,-125)

bob.width(20)
bob.begin_fill()
bob.left(55)
bob.forward(300)


for times in range(5):
    bob.left(45)
    bob.forward(50)
    bob.right(180)
    bob.forward(50)


jump(-75,-350)
bob.forward(200)
bob.right(180)
bob.forward(500)



bob.begin_fill()
bob.color("blue")
jump(340,50)
bob.circle(20)
bob.end_fill()
bob.width(5)
bob.color("green")
jump(330,50)
bob.begin_fill()
bob.forward(20)
bob.left(45)
bob.forward(10)
bob.left(45)
bob.forward(10)
bob.left(45)
bob.forward(10)
bob.left(45)
bob.left(45)
bob.forward(32)
bob.end_fill()


bob.begin_fill()
bob.color(0, 155, 255)
jump(240,20)
bob.circle(20)
bob.end_fill()
bob.width(5)
bob.color(0, 255, 204)
jump(245,20)
bob.begin_fill()
bob.forward(20)
bob.left(45)
bob.forward(10)
bob.left(45)
bob.forward(10)
bob.left(45)
bob.forward(10)
bob.left(45)
bob.left(45)
bob.forward(32)
bob.end_fill()



bob.begin_fill()
bob.color(155, 0, 255)
jump(540,90)
bob.circle(60)
bob.end_fill()
bob.width(5)
bob.color(204, 255, 0)
jump(530,90)
bob.begin_fill()
bob.forward(40)
bob.left(45)
bob.forward(30)
bob.left(45)
bob.forward(30)
bob.left(45)
bob.forward(30)
bob.left(45)
bob.left(45)
bob.forward(62)
bob.end_fill()



jump(100,100)
polygon(50,4,"grey")
jump(112,150)
bob.right(30)
polygon(50,3,"red")
jump(113,135)
polygon(10,4,"blue")
turtle.tracer(True)



