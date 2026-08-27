import turtle
from random import random
import math as mm

# Screen delay
screen = turtle.Screen()
t = turtle.Turtle()

# modify app name
t.screen.title('Golden Ratio')
screen.bgcolor("#2C2D2D")

#delay screen
screen.delay(1)
t.speed(1)

# generate goldern ratio
for i in range(600):
  #t.forward(i/1000)
  phi = (1 + mm.sqrt(i*i))/2
  t.forward(phi)
  t.right(phi)
  if i == 100:
    t.color('red')
  if i == 400:
    t.color('yellow')
  if i == 500:
    t.color('orange')
  print("i: ", i)


turtle.done()
