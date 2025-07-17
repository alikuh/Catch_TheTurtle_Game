import turtle
import random

pencere = turtle.Screen()
pencere.bgcolor("blue")
pencere.setup(width=860, height=600)
pencere.title("Turtle Game")
pencere.tracer(5)

# oyuncu özellikleri
oyuncu = turtle.Turtle()
oyuncu.pencolor("red")
oyuncu.color("white")
oyuncu.shape("triangle")
oyuncu.shapesize(2)
oyuncu.penup()

speed =1

# HEDEF KAPLUMBAĞALAR
turtle_list=[]
for i in range(5):
    hedef_turtle = turtle.Turtle()
    hedef_turtle.pencolor("green")
    hedef_turtle.color("green")
    hedef_turtle.penup()
    hedef_turtle.speed(0)
    hedef_turtle.shape("turtle")
    hedef_turtle.setposition(random.randint(-400, 400), random.randint(-300, 300))
    hedef_turtle.setheading(random.randint(0, 360))
    turtle_list.append(hedef_turtle)


# FONKSİYONLAR
def oyuncu_left():
    oyuncu.setheading(oyuncu.heading() + 30)
def oyuncu_right():
    oyuncu.setheading(oyuncu.heading() - 30)
def oyuncu_speed_up():
    global speed
    speed += 1
def oyuncu_speed_down():
    global speed
    speed -= 1
def oyuncu_stop():
    global speed
    speed = 0
def return_home():
    oyuncu.home()
def new_speed():
    global speed
    speed = 3

# Oyuncu harketleri
def oyuncu_go():
    oyuncu.forward(speed)
    if oyuncu.xcor() > 420 or oyuncu.xcor() < -420:
        return_home()
        new_speed()
    if oyuncu.ycor() > 290 or oyuncu.ycor() < -290:
        return_home()
        new_speed()
    pencere.update()
    pencere.ontimer(oyuncu_go, 50)

# SKOR SAYACI
skor = 0
yazi = turtle.Turtle()
yazi.hideturtle()
yazi.penup()
yazi.color("red")
yazi.goto(-400, 260)
yazi.write(f"SKOR : {skor} ", font=("Arial", 24, "bold"))


turtle.listen()
turtle.onkey(oyuncu_left, "Left")
turtle.onkey(oyuncu_right, "Right")
turtle.onkey(oyuncu_speed_up, "Up")
turtle.onkey(oyuncu_speed_down, "Down")
turtle.onkey(oyuncu_stop, "space")

oyuncu_go()
turtle.done()
