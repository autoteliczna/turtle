import turtle
import random 

t = turtle.Turtle()
t.speed(300)

bok = 250
odcinek = 83

def kwadrat():
  for i in range(4):
    t.fd(bok)
    t.rt(90)

kwadrat()
t.up()
t.fd(odcinek)
t.rt(90)
t.down()
t.fd(bok)
t.up()
t.lt(90)
t.fd(odcinek)
t.lt(90)
t.down()
t.fd(bok)

t.up()
t.rt(90)
t.fd(odcinek)
t.rt(90)
t.fd(odcinek)

t.rt(90)
t.down()
t.fd(bok)
t.up()
t.left(90)
t.fd(odcinek)
t.lt(90)
t.down()
t.fd(bok)
t.up()

t.goto(20,-63)
t.down()
t.write("X",font=("Arial", 50, "bold"))

t.up()
t.goto(100,-63)
t.down()
t.write("O",font=("Arial", 50, "bold"))

t.up()
t.goto(185,-63)
t.down()
t.write("X",font=("Arial", 50, "bold"))

t.up()
t.goto(20,-147)
t.down()
t.write("X",font=("Arial", 50, "bold"))

t.up()
t.goto(104,-147)
t.down()
t.write("X",font=("Arial", 50, "bold"))

t.up()
t.goto(182,-147)
t.down()
t.write("O",font=("Arial", 50, "bold"))

t.up()
t.goto(17,-230)
t.down()
t.write("O",font=("Arial", 50, "bold"))

t.up()
t.goto(104,-230)
t.down()
t.write("X",font=("Arial", 50, "bold"))

t.up()
t.goto(181,-230)
t.down()
t.write("O",font=("Arial", 50, "bold"))
