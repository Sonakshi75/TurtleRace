import random
from turtle import Turtle, Screen
t1 = Turtle(shape="turtle")
t2 = Turtle(shape="turtle")
t3 = Turtle(shape="turtle")
t4 = Turtle(shape="turtle")
t5 = Turtle(shape="turtle")
isRaceOn=False
screen = Screen()
screen.setup(width=500,height=400)
userBet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a colour(red/blue/pink/orange/green):")
print(userBet)
colours = ["red","blue","pink","orange","green"]
all_turtles=[]

t1.color(colours[0])
t1.penup()
t1.goto(x=-230,y=-100)
all_turtles.append(t1)

t2.color(colours[1])
t2.penup()
t2.goto(x=-230,y=-50)
all_turtles.append(t2)

t3.color(colours[2])
t3.penup()
t3.goto(x=-230,y=0)
all_turtles.append(t3)

t4.color(colours[3])
t4.penup()
t4.goto(x=-230,y=50)
all_turtles.append(t4)

t5.color(colours[4])
t5.penup()
t5.goto(x=-230,y=100)
all_turtles.append(t5)

if(userBet):
    isRaceOn=True

while(isRaceOn):
    for turtle in all_turtles:
        if turtle.xcor()>=220:
            isRaceOn = False
            winning_color = turtle.pencolor()
            if( winning_color == userBet ):
                print(f"You've won, {winning_color} is the winner")
            else:
                print(f"You have lost, {winning_color} is the winner")
        ram_distance = random.randint(0,10)
        turtle.forward(ram_distance)

screen.exitonclick()