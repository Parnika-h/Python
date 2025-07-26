import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

# TODO 1:Setup the screen
screen = Screen()
screen.setup(800, 600)
screen.title("My Pong Game")
screen.bgcolor("black")
screen.tracer(0)
# TODO 2:Create and move the paddle
paddle_1 = Paddle(350, 0)
paddle_2 = Paddle(-350, 0)
ball = Ball()
score = Score()
screen.listen()
screen.onkey(fun=paddle_1.up, key="Up")
screen.onkey(fun=paddle_1.down, key="Down")
screen.onkey(fun=paddle_2.up, key="w")
screen.onkey(fun=paddle_2.down, key="s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    # TODO 5:Detect collision with paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
    # TODO 6:Restart game after collision with right and left wall
    if ball.xcor() > 380:
        score.update_score1()
        ball.refresh()
    if ball.xcor() < -380:
        score.update_score2()
        ball.refresh()
screen.exitonclick()
