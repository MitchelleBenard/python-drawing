import turtle
t = turtle.Pen()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

# a new position
t.penup()
t.goto (150, 0)
t.pendown()

# a circle
t.circle(50)

# a new position
t.penup()
t.goto (-150, 0)
t.pendown()

# a rectangle
t.forward(60)
t.left(90)
t.forward(40)
t.left(90)
t.forward(60)
t.left(90)
t.forward(40)

