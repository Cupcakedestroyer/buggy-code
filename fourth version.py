#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
#body
painter.pensize(40)
painter.circle(20)
# end of body
# w = # of leg
# y = size of legs
# z = seperation of legs around circle
w = 4
y = 70
z = (45 / w)


painter.pensize(5)
n = 0
# n = amount of times can run before cut off
while (n < w):
  painter.goto(0,20)
  painter.setheading(z*n)
  painter.forward(y)
  n = n + 1

z = (45 / w)


painter.pensize(5)
n = 0
# n = amount of times can run before cut off
while (n < w):
  painter.goto(0,20)
  painter.setheading(180-z*n)
  painter.forward(y)
  n = n + 1

painter.penup()
painter.goto(10,40)
painter.pendown()
painter.pensize(3)
painter.color("blue")
painter.circle(3)
painter.penup()
painter.goto(-10,40)
painter.pendown()
painter.pensize(3)
painter.color("red")
painter.circle(3)





painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()