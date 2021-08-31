import turtle

wn = turtle.Screen()
wn.title("Pong by Piyius")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddel A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Function
def paddel_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddel_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddel_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddel_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddel_a_up, "w")
wn.onkeypress(paddel_a_down, "s")
wn.onkeypress(paddel_b_up, "Up")
wn.onkeypress(paddel_b_down, "Down")

# Main game loop
while True:
    wn.update()