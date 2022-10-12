from util import getTurtleAndScreen
# Drawing a checkerboard with turtle
# CAC, 2022

# For this one I determine the size of the screen by first realizing I want
# to break it up into an 8x8 grid of a given size square cell.
cellSize=120
numCols=8
numRows=8

# Compute the overall width and height.
width=cellSize*numCols
height = cellSize*numRows

# To make things easier, you can use my utility methods to get a turtle and screen.
# It will make it much easier to get the exact size screen you want with no extra
# space anywhere you don't want it. For some reason the default turtle stuff is
# flaky, and it seems to be impossible to get things to work exactly like you want
# without going through a lot of effort, which is why I did it for you.
turtle, screen = getTurtleAndScreen("Snowy Twilight",width,height,moveWorld=True)
# Make the background gray. Notice that we do not see any gray
# because the checkerboard covers the whole screen.
screen.bgcolor("magenta")

#Draw a curved sky line
#there are three layers of the sky line with three colors

#the first layer
turtle.penup()
turtle.goto(0, 4*cellSize)
turtle.pendown()
turtle.color("slate blue")
turtle.pensize(50)
turtle.begin_fill()
turtle.setheading(0)

def skyLine(i):
    while i < 8:
        turtle.forward(3.5 * cellSize)
        turtle.right(30)
        turtle.forward(30)
        turtle.left(30)
        turtle.forward(30)
        i = i + 1
skyLine(0)
#the second layer
turtle.penup()
turtle.goto(0, 4*cellSize - 50)
turtle.pendown()
turtle.color("LightSkyBlue")
turtle.pensize(50)
turtle.begin_fill()
turtle.setheading(0)
skyLine(0)

#the third layer
turtle.penup()
turtle.goto(0, 4*cellSize - 100)
turtle.pendown()
turtle.color("slate blue")
turtle.pensize(50)
turtle.begin_fill()
turtle.setheading(0)
skyLine(0)

#Draw the branches
turtle.penup()
turtle.goto(-2, 3.5 * cellSize)
turtle.pendown()

#the first branch
turtle.color("black")
turtle.pensize(10)
turtle.left(25)
turtle.forward(100)

#The method helps to draw the big branch with small branches
def tree(i):
    x = 0
    while x<i:
        turtle.left(30)
        turtle.forward(100)
        #branchOut(2)
        turtle.left(30)
        turtle.forward(100)
        turtle.backward(100)

        turtle.right(30)
        turtle.forward(100)
        turtle.right(30)
        turtle.forward(100)
        turtle.backward(100)
        x = x+1


tree(4)

#the second branch
turtle.penup()
turtle.goto(-2, 4 * cellSize)
turtle.pendown()


turtle.color("black")
turtle.pensize(1)
turtle.right(25)
turtle.forward(100)
tree(4)

#the third branch
turtle.penup()
turtle.goto(-2, 4.5 * cellSize)
turtle.pendown()

turtle.color("black")
turtle.pensize(5)
turtle.right(25)
turtle.forward(100)
tree(3)
#the forth branch
turtle.penup()
turtle.goto(-2, 3 * cellSize)
turtle.pendown()

turtle.color("black")
turtle.pensize(2)
turtle.left(75)
turtle.forward(100)
tree(3)


#draw the snow
for row in range (0,16):
    for col in range(0,16):
        turtle.penup()
        turtle.goto(col*cellSize/2+20,row*cellSize/2 +60)
        turtle.pendown()
        turtle.color("white")
        turtle.begin_fill()
        turtle.setheading(0)
        for i in range(0,4):
            turtle.forward(1.5)
            turtle.left(90)
        turtle.end_fill()


#draw the snow pile using circles
turtle.penup()
turtle.color("white")
turtle.goto(7.5*cellSize, -25)
turtle.pendown()
turtle.pensize(6)
turtle.begin_fill()
turtle.setheading(0)
turtle.circle(100, 1000)
turtle.end_fill()
#use while loop to draw multiple circles next to each other
i=0
while i<5:
    turtle.penup()
    turtle.color("white")
    turtle.goto(i * cellSize, -25)
    turtle.pendown()
    turtle.pensize(6)
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.circle(100, 1000)
    turtle.end_fill()
    i = i+1


screen.mainloop()