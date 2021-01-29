
import random
import turtle


screen = turtle.Screen()
screen.bgcolor('black')



class duong_vien(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("cyan")
        self.pensize(5)

    def ve(self):
        self.left(90)
        #self.penup()
        self.forward(200)
        self.pendown()
        self.left(90)
        self.forward(200)
        self.left(90)
        self.forward(400)
        self.left(90)
        self.forward(400)
        self.left(90)
        self.forward(400)
        self.left(90)
        self.forward(200)
        self.left(90)
        self.penup()
        self.forward(200)


#khởi tạo đối tượng vẽ đường viền
dv = duong_vien()
dv.ve()



class player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        #self.penup()
        self.speed(0)
        self.color("White")
        self.speed = 1
        self.shape("triangle")

    def move(self):
        self.forward(self.speed)
        #kiểm tra nếu va chạm đường biên thì quay đầu lại
        if (self.xcor()>200):
            self.setx(200)
            self.right(60)

        if (self.xcor()<-200):
            self.setx(-200)
            self.right(60)

        if (self.ycor()<-200):
            self.sety(-200)
            self.right(60)

        if (self.ycor()>200):
            self.sety(200)
            self.right(60)

    def giamtoc(self):
        self.speed -= 1
    def tangtoc(self):
         self.speed += 1
    def rephai(self):
        self.right(50)
    def retrai(self):
        self.left(50)

class monster(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        #self.penup()
        self.speed(0)
        self.color("red")





#khởi tạo đối tượng người chơi
p = player()

turtle.listen()
turtle.onkey(p.tangtoc,"Up")
turtle.onkey(p.giamtoc,"Down")
turtle.onkey(p.retrai,"Left")
turtle.onkey(p.rephai,"Right")



while True:
    p.move()
    










