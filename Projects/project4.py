# try to get as much grinders as you can, you can do this by getting enough beef to pay for the grinders by clicking space.
import turtle, time, random
from utils import *

set_background("cow")

beef = 0
grinder = 0
cost = 10
message_sprite = create_sprite("alien", -200,150)
message_sprite.hideturtle()
# Section 2 - controls
def get_beef():
    global beef
    beef+=1
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    create_sprite("beef",x,y)

def get_grinder():
    global beef,grinder,cost
    if beef>=cost:
        beef-=cost
        cost=cost * 2

        grinder+=1
        x=-400+120*grinder
        y=-250
        create_sprite("grinder",x,y)

        
        x=random.randint(-200,200)
        y=random.randint(-200,200)
      



window.onkeypress(get_beef, "space")
window.onkeypress(get_grinder, "c")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here
    if i % 50 ==0:
        beef+=grinder*4
    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")

    message_sprite.clear()
    message_sprite.write(f"beef: {beef}\ncost: {cost}\ngrinders: {grinder}",font=("Arial",30,"normal"))


    time.sleep(0.01)
    window.update()

# If ("grinder=5")
# message_sprite.write(f"Grinders: {grinders}\nCost: {cost},font=("Arial",30,"normal"))