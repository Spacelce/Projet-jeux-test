# Jeu python

import turtle 
import winsound

window = turtle.Screen()
window.title("Pong !!!")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)
# Score
score_a = 0
score_b = 0
# Raquette A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
# Raquette B
paddle_b = turtle.Turtle()
paddle_b .speed(0)
paddle_b .shape("square")
paddle_b .color("white")
paddle_b .shapesize(stretch_wid=5, stretch_len=1)
paddle_b .penup()
paddle_b .goto(350,0)
# Balle
ball = turtle.Turtle()
ball .speed(0)
ball .shape("square")
ball .color("white")
ball .penup()
ball .goto(0,0)
ball.dx = 0.2
ball.dy = 0.2
# Ligne milieu
for i in range(6):
    line = turtle.Turtle()
    line .speed(0)
    line .shape("square")
    line .color("white")
    line .shapesize(stretch_wid=2, stretch_len=0.5)
    line .penup()
    line .goto(0,235-(i*100))

# Affichage Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))
# Fonctions Raquettes
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down():        
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y) 

# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")

window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")

# Boucle principal du Jeu 
while True:
    window.update()
    # Mouvement de la balle 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Collisions avec les bordures
    if ball.ycor() > 290:
        winsound.PlaySound("Pong/ding2.wav", winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        winsound.PlaySound("Pong/ding2.wav", winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        winsound.PlaySound("Pong/ding1.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        score_a += 1
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        winsound.PlaySound("Pong/ding1.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        score_b += 1        
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    # Limites des Raquettes
    if paddle_a.ycor()+50 > 300:
        paddle_a.goto(-350,250)
    if paddle_a.ycor()-50 < -300:
        paddle_a.goto(-350,-250)
    if paddle_b.ycor()+50 > 300:
        paddle_b.goto(350,250)
    if paddle_b.ycor()-50 < -300:
        paddle_b.goto(350,-250)
    # Collisions avec les raquettes
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50) and (ball.ycor() > paddle_b.ycor() - 50):
        winsound.PlaySound("Pong/pong.wav", winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50) and (ball.ycor() > paddle_a.ycor() - 50):
        winsound.PlaySound("Pong/pong.wav", winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1
        
