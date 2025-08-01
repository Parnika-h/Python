from turtle import Screen,shape,Turtle
import pandas
t=Turtle()
t.penup()
t.hideturtle()
screen=Screen()
screen.title("The U.S. States Game")
screen.addshape("blank_states_img.gif")
shape("blank_states_img.gif")
data=pandas.read_csv("50_states.csv")
states=data.state.to_list()
game_is_on=True
while game_is_on:
    user=screen.textinput("Guess the state","Whats another states name?").title()
    if user=="Exit":
        break
    if user in states:
        x=data[data['state']==user]["x"]
        y=data[data['state']==user]["y"]
        t.goto(int(x),int(y))
        t.write(arg=user,move=False,align="Center",font=("Arial",8,"normal"))
        states.remove(user)
    if len(states)==0:
        game_is_on=False
new_data=pandas.DataFrame(states)
new_data.to_csv("States_left.csv")
screen.exitonclick()