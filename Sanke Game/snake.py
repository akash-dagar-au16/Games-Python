import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0
#Setup screen.
wn = turtle.Screen()
wn.title("Sanke Game by Akii Dagar")
wn.bgcolor("grey")
wn.setup(width=600, height=600)
wn.tracer(0)

#Sanke Head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake Food

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("Black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24 , "normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"



# Movement Function
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# KeyBoard bindings

wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")


# Main game loop

while True:
    wn.update()

    #Check For collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor() > 290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide Segments
        for segment in segments:
            segment.goto(1000,1000)

        #reset segments
        segments.clear()

        #Reset Delay
        delay = 0.1

        # Score Reset
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24 , "normal"))




    #check for food collision
    if head.distance(food) < 20 :
        #move the food
        x = random.randrange(-280,280, 20)
        y = random.randrange(-280,280, 20)
        food.goto(x,y)

        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("pink")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -=0.001

        # Increase score
        score += 1

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24 , "normal"))



    #move the end segment first
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    
    
    move()

    #check for head body collision

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
             # Hide Segments
            for segment in segments:
                 segment.goto(1000,1000)

            #reset segments
            segments.clear()

            #Reset Delay
            delay = 0.1

            #Score Reset
            score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24 , "normal"))


    time.sleep(delay)

wn.mainloop()