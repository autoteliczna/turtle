import turtle
import random 

t = turtle.Turtle()
t.speed(0)

def trojkat():
  for i in range(3):  
    t.fd(100)
    t.lt(120)
  
def trojkat2():
  t.up()
  t.fd(150)
  t.down()
  t.lt(120)
  for i in range(3):
    t.fd(100)
    t.rt(120)

n = int(input("ile: "))
for i in range(n):
 trojkat()
 trojkat2()

 t.rt(120)
 t.up()
 t.fd(50)
 t.down()
