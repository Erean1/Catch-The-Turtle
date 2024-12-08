import turtle
from random import randint

SMALL_FONT = ('Arial', 15, 'normal')
MEDIUM_FONT = ('Arial', 30, 'normal')
LARGE_FONT = ('Arial', 50, 'normal')


def change_position():
    t.hideturtle()
    x = randint(-300,300)
    y = randint(-300,300)
    t.goto(x,y)
    t.speed(10)
    t.showturtle()

def update_score():
    global score
    score += 1
    score_keeper.clear()
    score_keeper.goto(0, 250)
    score_keeper.write(f"Score: {score}",align="center",font=MEDIUM_FONT)

def update_time():
    time_keeper.clear()
    time_keeper.goto(0,210)
    if time > 0:
        time_keeper.write(f"Time: {time}",align="center",font=MEDIUM_FONT)

def target_clicked(x,y):
    if time > 0:
        update_score()
        change_position()

def action():
    global time
    time -= 1
    if time <= 0:
        score_keeper.clear()
        time_keeper.clear()
        t.hideturtle()
        time_keeper.color("red")
        time_keeper.write("TİME OVER",align="center",font=LARGE_FONT)
    else:
        update_time()
        win.ontimer(action,1000)

win = turtle.getscreen()
win.bgcolor("light blue")
win.title("turtle game")

score = 0
score_keeper = turtle.Turtle()
score_keeper.penup()
score_keeper.hideturtle()
score_keeper.setposition(0,250)
score_keeper.write(f"Score: {score}",align="center",font=MEDIUM_FONT)

time = 3
time_keeper = score_keeper.clone()
time_keeper.setposition(0,210)
time_keeper.write(f"Time: {time}",align="center",font=MEDIUM_FONT)


t = turtle.Turtle()
t.shape("turtle")
t.shapesize(2)
t.color("green")
t.penup()
t.setposition(randint(-300,300),randint(-300,300))

t.onclick(target_clicked)

action()

win.mainloop()