#Write a program that asks the user for the number of sides, the length of the side, the color, and the fill color of a regular polygon. 
#The program should draw the polygon and then fill it in.

import turtle

number_side = int(input('How many sides would you like?(Сколько сторон у вашей фигуры?) '))
angle = 360 / number_side
length_side = int(input('How long length side?(Какая будет длина стороны?) '))
color = input('Which color line do you want?(Каким цветом рисовать линии?) ')
fill_color = input('What color to sketch your figure?(Каким цветом закрасить вашу фигуру?) ')

wm = turtle.Screen()
turtle.color(color, fill_color)
turtle.begin_fill()
for i in range(number_side):

    turtle.fd(length_side)
    turtle.lt(angle)
turtle.end_fill()
turtle.exitonclick()
