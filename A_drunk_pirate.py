#A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps, turns another random amount, etc. 
#A social science student records the angle of each turn before the next 100 steps are taken. Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, -86. 
#(Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend. After the pirate is done walking, print the current heading. 
#Assume that the turtle originally has a heading of 0 and accumulate the changes in heading to print out the final. 
#Your solution should work for any sequence of experimental data.

import turtle

wn = turtle.Screen()
lovelace = turtle.Turtle()

# move the turtle forward a little so that the whole path fits on the screen
lovelace.penup()
lovelace.forward(60)

# now draw the drunk pirate's path
lovelace.pendown()
current_heading = 0
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:

    # we use .left() so that positive angles are counter-clockwise
    # and negative angles are clockwise
    current_heading = (current_heading + angle) % 360
    lovelace.left(angle)
    lovelace.forward(100)

# the .heading() method gives us the turtle's current heading in degrees
print("The pirate's final heading was", current_heading)

wn.exitonclick()
