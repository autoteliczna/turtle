import turtle
import random 

t = turtle.Turtle()


def kwadrat():
  for i in range(4):  
    t.fd(150)
    t.rt(90)
  
n = int(input("ile: "))
for i in range(n):
 kwadrat()

 t.up()
 t.fd(200)
 t.down()
