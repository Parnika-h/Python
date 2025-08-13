from turtle import Turtle,Screen
import random
c=""
race=False
turtles=[]
colors=["red","orange","yellow","green","blue","purple","violet"]
screen=Screen()
screen.setup(500,400)
user=screen.textinput("Make your bet","Which turtle will win the race?Enter a color: ")
for i in range(7):
    t=Turtle("turtle")
    t.penup()
    t.color(colors[i])
    t.goto(-230,-150+(i*50))
    turtles.append(t)
if user:
    race=True
while race:
    for t in turtles:
        t.forward(random.randint(0, 10))
        if t.xcor() > 230:
            race= False
            winner = t.pencolor()
            if winner == user:
                print(f"Yeah! You won 🎉 The {winner} turtle is the winner!")
            else:
                print(f"You lost 😢 The {winner} turtle won.")
            break

screen.exitonclick()