from turtle import Screen, Turtle
from  paddle import Paddle
from  ball import Ball
import  time

screen = Screen()
paddle = Turtle()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_padle = Paddle((350, 0))
l_padle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_padle.go_up, "Up")
screen.onkey(r_padle.go_down, "Down")
screen.onkey(l_padle.go_up, "w")
screen.onkey(l_padle.go_down, "s")

game_is_on = Turtle
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # collision with the top and down
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()




screen.exitonclick()