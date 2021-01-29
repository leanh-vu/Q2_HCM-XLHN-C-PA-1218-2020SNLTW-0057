



import turtle
import math
import random
import winsound
#-----------------------------------------------------
# Khai bao over game

over_pen = turtle.Turtle()
over_pen.speed(0)
over_pen.color("Cyan")
over_pen.penup()
over_pen.setposition(-200,50)
over_pen.hideturtle()
# Khai bao player win

win_pen = turtle.Turtle()
win_pen.speed(0)
win_pen.color("blue")
win_pen.penup()
win_pen.hideturtle

#thiet lap man hinh do hoa
sc = turtle.Screen()
#thiet lap hinh anh nen cao cho man hinh do hoa
sc.bgpic("space.gif")

#ve vung gioi han di chuyen
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pensize(3)
mypen.color("white")
mypen.speed(0)
for i in range(4):
    mypen.forward(600)
    mypen.left(90)
#ve xong , an doi tuong ve
mypen.hideturtle()
#tao ra nhan vat sieu anh hung
player = turtle.Turtle()
image="sieunhan.gif"
sc.addshape(image)
player.shape (image)
player.penup()
player.setposition(0,-250)
player.setheading(90)
playerspeed = 15

bulletspeed = 20
#trang thai sung sieu anh hung
bulletstate = "ready"
#--------------
#tao quai vat
bulletspeed_quaivat  = 20
enemy = turtle.Turtle()
image= "quaivat.gif"
sc.addshape(image)
enemy.shape(image)
enemy.penup()
enemy.speed(0)
enemy.setposition(0,180)
player.setheading(90)
enemyspeed = 15
bulletstate_quaivat="ready"
# sung cua sieu anh hung
bullet = turtle.Turtle()
bullet.color("blue")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5 , 0.5)
bullet.hideturtle()
#sung cua quai vat
gun = turtle.Turtle()
gun.color("black")
gun.shape("square")
gun.penup()
gun.speed(0)
gun.setheading(90)
gun.shapesize(0.5 , 0.5)
gun.hideturtle()
#Set the score to 0
score = 0
#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("Cyan")
score_pen.penup()
score_pen.setposition(-200, 200)
scorestring = "Player1: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#score quái vat
score_quaivat = 0
#Draw the score
score_pen_quaivat = turtle.Turtle()
score_pen_quaivat.speed(0)
score_pen_quaivat.color("Red")
score_pen_quaivat.penup()
score_pen_quaivat.setposition(200, 200)
scorestring_quaivat = "Player2: %s" %score_quaivat
score_pen_quaivat.write(scorestring_quaivat, False, align="left", font=("Arial", 14, "normal"))
score_pen_quaivat.hideturtle()
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    
    if (distance<20):
        return True
    else:
        return False


# Sung cua Sieu Nhan
def fire_bullet():

    #Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        print('change ready to fire')
        bulletstate = "fire"
        #Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

# Sung cu quai vat
def fire_bullet_quatvat():
    global bulletstate_quaivat
    if bulletstate_quaivat == "ready":
          bulletstate_quaivat = "fire"
          #Move the bullet to the just above the player
          x = enemy.xcor()
          y = enemy.ycor() + 10
          gun.setposition(x, y)
          gun.showturtle()
# định nghĩa các phím ra chuyển
def left():
    x = enemy.xcor()
    x -= enemyspeed
    if  x < -280:
        x = - 280
    enemy.setx(x)


def right():
    x = enemy.xcor()
    x += enemyspeed
    if x > 280:
        x = 280
    enemy.setx(x)



def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)




# khi nhấn phím

turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
turtle.onkey(left, "a")
turtle.onkey(right, "d")
turtle.onkey(fire_bullet_quatvat, "z")

turtle.listen()


#Main game loop
while True:
    
    

    #Check to see if the bullet has gone to the botton
    if gun.ycor() < -275:
            gun.hideturtle()
            bulletstate_quaivat = "ready"

    #Check for a collision between the bullet and the enemy
    if isCollision(gun, enemy):
            winsound.PlaySound('laser.wav', winsound.SND_FILENAME)
            #Reset the bullet
            gun.hideturtle()
            bulletstate = "ready"
            gun.setposition(0, -400)
            #Update the score
            score += 10
            scorestring = "Player1: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
   
    if (score == 150):
        winsound.PlaySound('win.wav', winsound.SND_FILENAME)
        player.hideturtle()
        enemy.hideturtle()
        print ("Victory")
        break
    if (score_quaivat == 150):
        winsound.PlaySound('over.wav', winsound.SND_FILENAME)
        player.hideturtle()
        enemy.hideturtle()
        print ("Game Over")
        break
    #Move the bullet
    if (bulletstate == "fire"):
        print('bullet move')
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    #Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"















































































