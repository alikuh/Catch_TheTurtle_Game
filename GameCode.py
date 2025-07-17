import turtle

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
def ouyuncu_stop():
    global speed
    speed = 0
def return_home():
    oyuncu.home()


# Oyuncu harketleri
def oyuncu_go():
    oyuncu.forward(speed)
    if oyuncu.xcor() > 400 or oyuncu.xcor() < -400:
        return_home()
    if oyuncu.ycor() > 280 or oyuncu.ycor() < -280:
        return_home()
    pencere.update()
    pencere.ontimer(oyuncu_go, 50)




turtle.listen()
turtle.onkey(oyuncu_left, "Left")
turtle.onkey(oyuncu_right, "Right")
turtle.onkey(oyuncu_speed_up, "Up")
turtle.onkey(oyuncu_speed_down, "Down")
oyuncu_go()
turtle.done()