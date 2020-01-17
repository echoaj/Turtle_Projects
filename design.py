import turtle as t
t.speed(0)
t.color("blue")

for i in range(25):
    for j in range(6):
        t.forward(100)
        t.right(60)
    t.right(15)


t.Screen().exitonclick()