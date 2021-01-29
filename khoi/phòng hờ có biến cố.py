

import turtle
import math
import random
import winsound
import time
#------thiet lap ban dau
over_pen = turtle.Turtle()
over_pen.speed(0)
over_pen.color("yellow")
over_pen.penup()
over_pen.setposition(-200,50)
over_pen.hideturtle()
win_pen = turtle.Turtle()
win_pen.speed(0)
win_pen.color("yellow")
win_pen.penup()
win_pen.setposition(-200,50)
win_pen.hideturtle()
# thiết lập màn hình
sc = turtle.Screen()
sc.bgpic("space.gif")
# Vẽ vùng giới hạn di chuyển:
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
mypen.speed(0)

#----- Tạo ra nhân vật siêu anh hùng
player = turtle.Turtle()
image="pp1.gif"
sc.addshape(image)
player.shape(image)
player.penup()
player.setposition(0, -250)
player.setheading(90)


playerspeed = 15
bulletspeed = 20

#trang thai sung Sieu anh hùng
bulletstate = "ready"


#---------------------------
# Tao ra quai vat
bulletspeed_quaivat = 20
enemy = turtle.Turtle()
image4="p2.gif"
sc.addshape(image4)
enemy.shape(image4)
enemy.penup()
enemy.speed(0)
enemy.setposition(random.randint(-300, 300), random.randint(-100, 300))

enemyspeed = 2
bulletstate_quaivat="ready"

# Vẽ vùng giới hạn di chuyển:
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
mypen.speed(0)
for i in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#Create the player's bullet
bullet = turtle.Turtle()
image5="dan1.gif"
sc.addshape(image5)
bullet.shape(image5)
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

#sung cua quai vat

sung = turtle.Turtle()
sung.color("red")
sung.shape("circle")
sung.penup()
sung.speed(0)
sung.setheading(90)
sung.shapesize(0.5, 0.5)
sung.hideturtle()

#Set the score to 0
score = 0
#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("orange")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Player: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#score quái vat
score_quaivat = 0
#Draw the score
score_pen_quaivat = turtle.Turtle()
score_pen_quaivat.speed(0)
score_pen_quaivat.color("pink")
score_pen_quaivat.penup()
score_pen_quaivat.setposition(200, 280)
scorestring_quaivat = "Enemy: %s" %score_quaivat
score_pen_quaivat.write(scorestring_quaivat, False, align="left", font=("Arial", 14, "normal"))
score_pen_quaivat.hideturtle()   

# định nghĩa các phím ra chuyển
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
	
def move_down():
	y = player.ycor()
	y -= playerspeed
	if y < -280:
		y = - 280
	player.sety(y)

	
def move_up():
	y = player.ycor()
	y += playerspeed
	if y > 280:
		y = 280
	player.sety(y)



def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    
    if (distance<20):
        return True
    else:
        return False
    
def boundaryChecking(t):
    if t.xcor() < -300 or t.xcor() > 300:
        t.right(180)
        t.setposition(random.randint(-300, 300), random.randint(-300, 300))
    if t.ycor() < -300 or t.ycor() > 300:
        t.right(180)
        t.setposition(random.randint(-300, 300), random.randint(-300, 300))

# Sung cua Sieu Nhan
def fire_bullet():
    
    #Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
          bulletstate = "fire"
          #Move the bullet to the just above the player
          x = player.xcor()
          y = player.ycor() + 10
          bullet.setposition(x, y)
          bullet.showturtle()

# Sung cua quai vat
def fire_bullet_quatvat():
    #Declare bulletstate as a global if it needs changed
    global bulletstate_quaivat
    if bulletstate_quaivat == "ready":
          bulletstate_quaivat = "fire"
          #Move the bullet to the just above the player
          x = enemy.xcor()
          y = enemy.ycor() + 10
          sung.setposition(x, y)
          sung.showturtle()


# khi nhấn phím

turtle.onkey(move_left, "a")
turtle.onkey(move_right, "d")
turtle.onkey(move_up, "w")
turtle.onkey(move_down, "s")
turtle.onkey(fire_bullet, "space")

turtle.listen()


#Main game loop
while True:
   
    #Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    # quai vat ban
    fire_bullet_quatvat()
    #Move the bullet_quaivat
    if (bulletstate_quaivat == "fire"):
            y = sung.ycor()
            y -= bulletspeed_quaivat
            sung.sety(y)
                
    #Check to see if the bullet has gone to the botton
    if sung.ycor() < -300:
            sung.hideturtle()
            bulletstate_quaivat = "ready"
    
   
#Move the enemy back and down
    if enemy.xcor() > 280:
    #Move all enemies down
	
            y = enemy.ycor()
            y -= 40
            enemy.sety(y)
            #Change enemy direction
            enemyspeed *= -1
		
    if enemy.xcor() < -280:
        #Move all enemies down
	
            y = enemy.ycor()
            y -= 40
            enemy.sety(y)
            #Change enemy direction
            enemyspeed *= -1
			
    

    #Check for a collision between the bullet and the enemy
    if isCollision(bullet, enemy):
            winsound.PlaySound('laser.wav', winsound.SND_FILENAME)
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Update the score
            score += 10
            scorestring = "Player: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
    #va cham giua Dan va sieu anh hung
    if isCollision(sung, player):
            winsound.PlaySound('laser.wav', winsound.SND_FILENAME)
           #Reset the bullet
            sung.hideturtle()
            bulletstate_quaivat = "ready"

            
            bullet.setposition(0, -400)
           #Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Update the score
            score_quaivat += 10
            scorestring_quaivat = "Enemy: %s" %score_quaivat
            score_pen_quaivat.clear()
            score_pen_quaivat.write(scorestring_quaivat, False, align="left", font=("Arial", 14, "normal"))
    # va cham nguoi choi va quai vat        
    if isCollision(player, enemy):
            winsound.PlaySound('over.wav', winsound.SND_FILENAME)
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over")
            break
    if (score == 150):
        winsound.PlaySound('over.wav', winsound.SND_FILENAME)
        player.hideturtle()
        enemy.hideturtle()
        print ("Game Over")
        print ("YOU WIN")
        break
    if (score_quaivat == 50):
        winsound.PlaySound('over.wav', winsound.SND_FILENAME)
        player.hideturtle()
        enemy.hideturtle()
        print ("Game Over")
        break
    #Move the bullet
    if (bulletstate == "fire"):
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)
    #Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"

            


	
		
