import turtle
import random
import time


delay=0.1
score=0
highestscore=0

bodies=[]

s=turtle.Screen()
s.title("90s Snake Game")
s.bgcolor("gray")
s.setup(width=600,height=600)

head=turtle.Turtle()
head.speed(0)
head.color("white")
head.shape("square")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction="stop"

food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.goto(0,200)
food.ht()
food.st()

sb=turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("score:0 | Heighest score: 0")


def moveup():
    if head.direction!="down":
       head.direction="up"

def movedown():
    if head.direction!="up":
        head.direction="down"
def moveright():
    if head.direction!="left":
        head.direction="right"

def moverleft():
    if head.direction!="right":
        head.direction="left"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        y=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        y=head.xcor()
        head.setx(x-20)

s.listen()
s.onkey(moveup,"up")
s.onkey(movedown,"down")
s.onkey(moverleft,"left")
s.onkey(moveright,"right")


while True:
    s.updatee()
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)

        if head.distance(food)<20:
            x=random.randint(-290,290)
            y=random.randint(-290,290)
            food.goto(x,y)

            body=turtle.Turtle()
            body.speed(0)
            body.shape("square")
            body.color("red")
            body.fillcolor("black")
            bodies.append(body)

            score+=10
            delay-=0.001

            if score>highestscore:
                highestscore=score
            sb.clear()
            sb.write("score: {}Highest Score: {}".formt(score,highestscore))
        for index in range(len(bodies)-1,0,-1):
            x=bodies[index-1].xcor()
            y=bodies[index-1].ycor()
            bodies[index].goto(x,y)

        if len(bodies)>0:
            x=head.xcor() 
            y=head.ycor()
            bodies[0].goto(x,y)
        move()

        for body in bodies:
            if body.distance(head)<20:
                time.sleep(1)
                head.goto(0,0)
                head.direction="stop"

                for body in bodies:
                    body.ht()
                bodies.clear()

                score=0
                delay=0.1
                sb.clear()
                sb.write("score: {} Highest score: {}".format)
            time.sleep(delay)
        s.mainloop()


