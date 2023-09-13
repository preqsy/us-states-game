import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state = []
data = pandas.read_csv("50_states.csv")
# answer_state = turtle.textinput(title="Guess The U.S State", prompt="Guess another state").capitalize()
t = turtle.Turtle()
while len(guessed_state) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_state)}/50", prompt="Guess another state").title()
    if answer_state == "Exit":
        missing_states = [state for state in data.state if state not in guessed_state]
        df = pandas.DataFrame(missing_states)
        df.to_csv("missed_states.csv")
            
        break
    if answer_state in str(data.state):
        if answer_state in guessed_state:
            pass
        else:
            guessed_state.append(answer_state)
        state_data = data[data.state == answer_state]
        new_x = state_data.x
        state_data = data[data.state == answer_state]
        new_y = state_data.y
        print(type(int(new_x)))
        t.penup()
        t.goto(int(new_x), int(new_y))
        t.write(f"{answer_state}")
        

        