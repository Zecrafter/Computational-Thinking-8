you=input("enter your name;")
resturant = input("type your favorite resturant; ") 
food=input("now what is your favorite food?; ")
name=input("and pick a name please; ")
print("pick one")
getaway=input("swam, drove, or rolled ") 
name2=input("now pick another name")
print(f"on a nice day, there was food being prepped in {resturant}, but one poor little {food} named {name} shivered beneath the gaping mouth of {name2}, who had taken him on a tray and held untensils.")
print(f"as poor {name} was raised up high into the air, he violently twisted away, somehow managed to leap next to the car parked on the beach and he {getaway} away")
print(f"{you} saw this and reasonably called the police")
print(f"as {name} {getaway} as fast as he could, the police helicopters lights shone down on him, connfining him to his ground, soon entrapped by the police as they glided down to him")
print(f"{name} woke abruptly, intact but lost. bars, walls but no windows. Prison?")
if getaway== "swam":
    print("he snuck around his cell, rolled to the gaurd and threw a pebble at him then ran as fast as his legs could carry him out the exit")
else:
    place=input("where to? example; field, underwater layer, home")
    print(f"then, {food} flew to his {place}")
    real=input("choose one; who was the real villain? the grinch, the flinch, the singer, or the tree?")
    if real== "the grinch":
        print("correct you won")
    else:
        print("sorry you lost")