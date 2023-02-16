from turtle import *

def square(sidelenght = 100):
    for j in range(4):
        forward(sidelenght)
        right(90)

def triangle(sidelength = 100):
    for i in range(3):
        right(120)
        forward(sidelength)


def polygon(sides = 4, lenght = 100):
    angle = 360/sides
    for i in range(sides):
        right(angle)
        forward(lenght)

def star(length = 100):
    for i in range(5):
        forward(length)
        right(144)  
    
def starspiral():
    length = 100
    for i in range(60):
        star(length)
        right(5)
        length = length + 5
        
shape('turtle')
speed(0)

starspiral()

#star(200)


#polygon(8,200)
#triangle(200)

"""
square(30)
square(50)
square()
"""
"""
for i in range(60):
    square()
    right(5)
"""
"""
length = 100
for i in range(60):
    square(length)
    right(5)
    length = length + 5
"""
