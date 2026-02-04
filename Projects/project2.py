kindness_points=0
nonchalant_points=0
heartless_points=0

answer1 = input("if a little kid waved at you, would you; A- wave back an smile, B- walk past, or C- teach him a lesson not to wave at strangers")
if answer1== "A":
    kindness_points += 1
if answer1== "B":
    nonchalant_points +=1
if answer1=="C"or "B":
    heartless_points +=1


answer2=input("someone drops a old book and the pages go everywhere do you A- walk past, B- help clean it up  or C- kick the papers")
if answer2== "A":
    nonchalant_points +=1
if answer2== "B":
    kindness_points +=2
if answer2== "C":
    heartless_points +=2

answer3=input("someone drops a couple 10 dollar bills, you pick it up do you A- tell them they dropped some money and give it back to them, B- take the money or C- take some of it and give him the rest")
if answer3== "A":
    kindness_points+=1
if answer3== "B":
    heartless_points+=1
if answer3== "C":
    nonchalant_points+=2


print(f" your kindness is {kindness_points}, your meanness is {heartless_points}, and you nonchalance is a {nonchalant_points}")
#End: three different types of points
if kindness_points> heartless_points and kindness_points> nonchalant_points:
    print("You are a kind person")
elif heartless_points> kindness_points and heartless_points> nonchalant_points:
    print("you are unempathetic")
elif nonchalant_points> kindness_points and nonchalant_points> heartless_points:
    print("you are very slick dude.")
