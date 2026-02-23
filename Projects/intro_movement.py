import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("character1",0,-200)
s2 = create_sprite("character2",0, 0)
# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 2
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 2
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 2
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 2
    y = s1.ycor() 
    s1.goto(x,y)

def move_up2():
    x = s2.xcor()
    y = s2.ycor() + 2
    s2.goto(x,y)
        
def move_down2():
    x = s2.xcor()
    y = s2.ycor() - 2
    s2.goto(x,y)
    
def move_left2():
    x = s2.xcor() - 2
    y = s2.ycor() 
    s2.goto(x,y)
    
def move_right2(): 
    x = s2.xcor() + 2
    y = s2.ycor() 
    s2.goto(x,y)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "a")
window.onkeypress(move_up2, "Up")
window.onkeypress(move_down2, "Down")
window.onkeypress(move_right2, "Left")
window.onkeypress(move_left2, "Right")
def draw ():
    s1.pendown()

def stop draw ():
    s1penup()



window.onkeypress(draw, "c")
window.onkeyrelease(stop draw, "c")
# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(show, "h")
window.onkeyrelease(hide, "h")


# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    
    # TODO - add code for automatic actions


    # TODO - make an if statement for ending the game

    
    time.sleep(0.01)
    window.update()
    

	
print("Game Over")