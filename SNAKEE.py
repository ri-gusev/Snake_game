import turtle, time, random

wn = turtle.Screen()
wn.screensize(600,600,'black')
wn.colormode(255)
wn.title('SNAKE')
wn.tracer(0)

#Декорации для игры
dec = turtle.Turtle()
dec.speed(0)
dec.shape('turtle')
dec.hideturtle()
dec.color('white')
dec.penup()
dec.goto(388,330)
dec.pendown()
dec.goto(-388,330)
dec.goto(-388,-320)
dec.goto(388,-320)
dec.goto(388,330)

# Звездочки на заднем фоне
for i in range(30):
    dec.penup()
    dec.goto(random.randint(-300,300),random.randint(-300,300))
    dec.pendown()
    dec.circle(random.randint(0,3))


#Main_character
mn = turtle.Turtle()
mn.speed(9)
mn.shape('turtle')
mn.color('white')
mn.penup()
mn.home()
mn.direction = 'stop' 
#это не команды из библиотеки, 
#мы как бы создаем новую переменныю чтобы хранить там направление черепашки
#Например стоп - черепашка не двигается или старт - черепашка начала движение

#Pirate
pr = turtle.Turtle()
pr.shape('turtle')
pr.shapesize(2,2,0)
pr.color('red')
pr.penup()
pr.goto(600,600)

#Pirate2
pr2 = turtle.Turtle()
pr2.shape('turtle')
pr2.shapesize(2,2,0)
pr2.color('green')
pr2.penup()
pr2.goto(-600,600)


#Gold
gl = turtle.Turtle() 
gl.shape('circle')
gl.color('yellow')
gl.penup()
gl.goto(0,100)

score = 0
high_score = 0
delay = 0.1
x = 0
y = 0

# Создаем черепашку для отрисовки табло со счетом
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.hideturtle()
pen.penup()
pen.goto(0,260)
pen.pendown() 
pen.write(f'Счет: {score}           Рекорд: {high_score}', align='center', font = ('Courier', 18, 'normal'))

def move_up():
    mn.direction = 'Up'
    mn.setheading(90)
def move_down():
    mn.direction = 'Down'
    mn.setheading(270)
def move_left():
    mn.direction = 'Left'
    mn.setheading(180)
def move_right():
    mn.direction = 'Right'
    mn.setheading(0)

def check():
    if mn.direction == 'Up':
        y = mn.ycor()
        y = mn.sety(y + 20)
    if mn.direction == 'Down':
        y = mn.ycor()
        y = mn.sety(y - 20)
    if mn.direction == 'Left':
        x = mn.xcor()
        x = mn.setx(x - 20)
    if mn.direction == 'Right':
        x = mn.xcor()
        x = mn.setx(x + 20)

wn.listen()
wn.onkeypress(move_up,'Up')
wn.onkeypress(move_down,'Down')
wn.onkeypress(move_left,'Left')
wn.onkeypress(move_right,'Right')
def loose():
    global score
    time.sleep(1)
    mn.direction = 'stop'
    mn.home()
    pr.goto(600,600)
    pr2.goto(-600,600)
    score = 0
    pen.clear()
    pen.write(f'Счет: {score}           Рекорд: {high_score}', align='center', font = ('Courier', 18, 'normal'))
    
while True:
    wn.update()
    if mn.xcor()> 360 or mn.xcor()< -360 or mn.ycor() >295 or mn.ycor() <-290:
       loose()    
    check()
    time.sleep(delay)

    if mn.distance(gl) < 20:  #Если расстояние от центра стрелочки до центра монетки меньше 20 пикселей
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        gl.goto(x,y)
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f'Счет: {score}           Рекорд: {high_score}', align='center', font = ('Courier', 18, 'normal'))
    
    if score >=10:
        pr.showturtle()
        pr.setheading(pr.towards(mn.xcor(),mn.ycor()))   #Враг смотрит в сторонуглавного героя
        if score<100:
            pr.fd(4)
        elif score>=100:
            pr.fd(7)
        elif score>=120:
            pr.fd(10)
        if mn.distance(pr) < 25:
            loose()

    
    if score >= 100:
        pr2.showturtle()
        pr2.setheading(pr2.towards(mn.xcor(),mn.ycor()))   #Враг смотрит в сторонуглавного героя
        if score<100:
            pr2.fd(6)
        elif score>=100:
            pr2.fd(8)
        elif score>=120:
            pr2.fd(8)
        if mn.distance(pr2) < 25:
            loose()      
            


turtle.mainloop()