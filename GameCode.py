import turtle
import random
import winsound

# PENCERE ÖZELLİKLERİ
pencere = turtle.Screen()
pencere.setup(width=860, height=600)
pencere.title("Turtle Game")
pencere.tracer(5)

# oyuncu özellikleri
oyuncu = turtle.Turtle()
oyuncu.pencolor("red")
oyuncu.color("gray")
oyuncu.shape("triangle")
oyuncu.shapesize(2)
oyuncu.penup()
oyuncu.hideturtle()
speed =1

# BİLGİ PANELİ
panel = turtle.Turtle()
panel.hideturtle()
panel.penup()
panel.goto(-430, 300)  # sol üst köşe
panel.pendown()
panel.color("yellow")  # panelin arka plan rengi
panel.begin_fill()
for _ in range(2):
    panel.forward(860)  # pencere genişliği
    panel.right(90)
    panel.forward(40)   # panel yüksekliği
    panel.right(90)
panel.end_fill()
panel.penup()

def kenar_ciz():
    kenar = turtle.Turtle()
    kenar.hideturtle()
    kenar.speed(0)
    kenar.color("red")
    kenar.pensize(5)
    kenar.penup()

    # Sol kenar
    kenar.goto(-425, 260)
    kenar.pendown()
    kenar.goto(-425, -290)
    kenar.penup()

    # Sağ kenar
    kenar.goto(420, 260)
    kenar.pendown()
    kenar.goto(420, -290)
    kenar.penup()

    # Üst kenar
    kenar.goto(-420, 260)
    kenar.pendown()
    kenar.goto(420, 260)
    kenar.penup()

    # Alt kenar
    kenar.goto(-420, -290)
    kenar.pendown()
    kenar.goto(420, -290)
kenar_ciz()

# SKOR SAYACI
skor = 0
yazi = turtle.Turtle()
yazi.hideturtle()
yazi.penup()
yazi.color("red")
yazi.goto(-400, 260)
yazi.write(f"SKOR :{skor} ", font=("Arial", 24, "bold"))

# GERİ SAYIM
zaman =80
yazi2 = turtle.Turtle()
yazi2.hideturtle()
yazi2.penup()
yazi2.color("black")
yazi2.goto(-220, 260)
yazi2.write(f"SÜRE : {zaman} ", font=("Arial", 24, "bold"))

# CAN SAYACI
can = 5
yazi3 = turtle.Turtle()
yazi3.hideturtle()
yazi3.penup()
yazi3.color("red")
yazi3.goto(300, 260)
yazi3.write(f"CAN : {can} ", font=("Arial", 24, "bold"))

# HEDEF KAPLUMBAĞALAR
turtle_list=[]
for i in range(6): # hedeflerin sayisinin ayari
    hedef_turtle = turtle.Turtle()
    hedef_turtle.pencolor("green")
    hedef_turtle.color("green")
    hedef_turtle.penup()
    hedef_turtle.speed(0)
    hedef_turtle.shape("turtle")
    hedef_turtle.setposition(random.randint(-390, 390), random.randint(-290, 240))
    hedef_turtle.setheading(random.randint(0, 360))
    turtle_list.append(hedef_turtle)

#HEDEF HAREKETLERİ
def hedef_hareket_ettir():
    for hedef in turtle_list:
        hedef.forward(5) # hedeflerin hareket hızı ayari

        # Eğer hedef ekran dışına çıkarsa, herhangi biryerde tekrar doğsun
        if hedef.xcor() > 440 or hedef.xcor() < -400 or hedef.ycor() > 260 or hedef.ycor() < -320:
            hedef.setposition(random.randint(-400, 400), random.randint(-300, 300))
            hedef.setheading(random.randint(0, 360))
    pencere.ontimer(hedef_hareket_ettir, 50)

# FONKSİYONLAR
def oyuncu_left():
    oyuncu.setheading(oyuncu.heading() + 30)
def oyuncu_right():
    oyuncu.setheading(oyuncu.heading() - 30)
def oyuncu_speed_up():
    global speed
    speed += 2
def oyuncu_speed_down():
    global speed
    speed -= 2
def oyuncu_stop():
    global speed
    speed = 0
def return_home():
    oyuncu.home()
def new_speed():
    global speed
    speed = 3
def game_over():
    oyuncu.hideturtle()
    yazi4 = turtle.Turtle()
    yazi4.hideturtle()
    yazi4.color("red")
    yazi4.penup()
    yazi4.goto(-100, 0)
    yazi4.write("GAME OVER", font=("Arial", 24, "bold"))
    oyuncu.speed(0)
# Oyuncu harketleri
def oyuncu_go():
    oyuncu.forward(speed)
    if oyuncu.xcor() > 420 or oyuncu.xcor() < -420:
        winsound.PlaySound("dead_sound.wav", winsound.SND_ASYNC)
        return_home()
        new_speed()
        can_sayim()
    if oyuncu.ycor() > 250 or oyuncu.ycor() < -290:
        winsound.PlaySound("dead_sound.wav", winsound.SND_ASYNC)
        return_home()
        new_speed()
        can_sayim()
    pencere.update()
    pencere.ontimer(oyuncu_go, 50)

def geri_sayim():
    global zaman
    if zaman>0 :
        zaman -=1
        yazi2.clear()
        yazi2.write(f"SÜRE : {zaman} ", font=("Arial", 24, "bold"))
        pencere.ontimer(geri_sayim, 1000) # saniyede bir yeniler
    else:
        yazi2.clear()
        yazi2.write(f"SÜRE BİTTİ",font=("Arial", 24, "bold"))
        oyuncu.hideturtle() # oyuncu artık görünmez.

def can_sayim():
    global can
    can -=1
    yazi3.clear()
    if can<=0:
        yazi3.write(f"CAN : {0} ", font=("Arial", 24, "bold"))
        game_over()
    else:
        yazi3.write(f"CAN : {can} ", font=("Arial", 24, "bold"))

def carpma_kontrolu():
    global skor
    for hedef in turtle_list:
        if oyuncu.distance(hedef) < 30 :
            skor += 1
            yazi.clear()
            winsound.PlaySound("yeme_sesi.wav",winsound.SND_ASYNC)
            yazi.write(f"SKOR :{skor} ", font=("Arial", 24, "bold"))
            hedef.setposition(random.randint(-400, 400), random.randint(-300, 300))
            hedef.setheading(random.randint(0, 360))
    pencere.ontimer(carpma_kontrolu,100)

def start():
    oyuncu.showturtle()
    start_screen.clear()
    pencere.bgcolor("pink")
    oyuncu_go()
    geri_sayim()
    hedef_hareket_ettir()

# BAŞLANGIÇ EKRANI
pencere.bgcolor("gray")
start_screen = turtle.Turtle()
start_screen.penup()
start_screen.hideturtle()
start_screen.pencolor("black")
start_screen.goto(-400,-90)
start_screen.write("SAĞ ve SOL TUŞLARI İLE YÖN VER\n"
                   "Q ile HIZLAN\n"
                   "E ile YAVAŞLA\n"
                   "SPACE ile DUR\n\n"
                   f"HAZIRSAN ENTER'e BAS VE 80 SANİYEDE \nCANLARINI BİTİRMEDEN YAPABİLECEĞİN\nEN İYİ SKORU YAP",
                   font=("Arial",27,"bold"))

turtle.listen()
turtle.onkey(oyuncu_left, "Left")
turtle.onkey(oyuncu_right, "Right")
turtle.onkey(oyuncu_speed_up, "q")
turtle.onkey(oyuncu_speed_down, "e")
turtle.onkey(oyuncu_stop, "space")
turtle.onkey(start,"Return")

carpma_kontrolu()
turtle.done()
