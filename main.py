import turtle
import pandas
screen=turtle.Screen()
screen.title("India States Game")
image="blankmap.gif"
turtle.addshape(image)
turtle.shape(image)

data=pandas.read_csv("istates2.csv")
all_states=data.state.to_list()
guess_states=[]
while len(guess_states)<29:
    ans_state=screen.textinput(title=f"{len(guess_states)}/29 correct",prompt="Whats the state name?").title()
    if ans_state=="Exit":
        missing_states=[state for state in all_states if state not in guess_states]
        new=pandas.DataFrame(missing_states)
        new.to_csv("new_st.csv")
        break
    if ans_state in all_states:
        guess_states.append(ans_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        res = data[data.state == ans_state]
        x_cor = int(res.x)
        y_cor = int(res.y)
        t.goto(x_cor,y_cor)
        t.write(ans_state)

screen.exitonclick()
