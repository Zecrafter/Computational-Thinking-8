set_background("castle")
x1 =-300
y1 =-0
x2 =-300
y2 =-100
x3 =-300
y3 =100
x4 =-300
y4 =200
t1 = create_sprite("turtle",x1,y1)
t2 = create_sprite("turtle",x2,y2)
t3 = create_sprite("turtle",x3,y3)
t4 = create_sprite("turtle",x4,y4)

#     x1 +=8
#     x2 +=9
#     x3 +=7
#     x4 +=random.radient(4,11)

#     t1.goto(x1, y1)
#     t2.goto(x2, y2)
#     t3.goto(x3, y3)
#     t4.goto(x4, y4)

#     window.update()
#     time.sleep(0.1)
x1 >= x2 and x1 >= x3 and x1 >= x4:
     print("player 1 wins!")
x3 >= x2 and x3 >= x1 and x3 >= x4:
    print("player 3 wins!")
x4 >= x2 and x4 >= x3 and x4 >= x1:
     print("player 4 wins!")
 elif
     print("player 2 wins!")