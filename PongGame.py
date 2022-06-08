from turtle import Turtle
import time



#----------------------------------------------------------------------------------------------------------------
#Creating class paddle:

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

#---------------------------------------------------------------------------------------------------------------------

#creating class Ball:
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move= 10
        self.move_speed = 0.1



    def move(self):
        new_x = self.xcor()+ self.x_move
        new_y = self.ycor()+ self.y_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed= 0.1
        self.bounce_x()

#------------------------------------------------------------------------------------------------------------------------
#creating scoreboard:


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()       
        
#-------------------------------------------------------------------------------------------------------------------------------       
#main program for game:

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PADDLE_GAME")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard= Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on= True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #detecting collision with wall
    if ball.ycor()> 280 or ball.ycor()< -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle)< 50 and ball.xcor()> 320 or ball.distance(l_paddle) < 50 and ball.xcor()< -320:
        ball.bounce_x()

     # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
        
------------------------------------------end end----------------------------------------------------------------------------------

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
        
        
