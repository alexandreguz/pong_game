from turtle import Screen, Turtle
from  paddle import Paddle
from  ball import Ball
from scoreboard import Scoreboard
import  time


screen = Screen()
paddle = Turtle()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_padlle = Paddle((350, 0))
l_padlle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_padlle.go_up, "Up")
screen.onkey(r_padlle.go_down, "Down")
screen.onkey(l_padlle.go_up, "w")
screen.onkey(l_padlle.go_down, "s")

game_is_on = Turtle
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # collision with the top and down
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with r_paddle
    if ball.distance(r_padlle) < 50 and ball.xcor() > 320 or ball.distance(l_padlle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()