#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
x = trtl.Turtle()
#body
x.pensize(40)
x.circle(20)
# end of body
# w = # of leg
# y = size of legs
# z = seperation of legs around circle
w = 8
y = 70
z = 360 / w

x.pensize(5)
n = 0
# n = amount of times can run before cut off
while (n < w):
  x.goto(0,20)
  x.setheading(z*n)
  x.forward(y)
  n = n + 1
x.hideturtle()
wn = trtl.Screen()
wn.mainloop()