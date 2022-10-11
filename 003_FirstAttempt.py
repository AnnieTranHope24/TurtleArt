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

#Draw the sky line
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

turtle.penup()
turtle.goto(0, 4*cellSize - 50)
turtle.pendown()
turtle.color("LightSkyBlue")
turtle.pensize(50)
turtle.begin_fill()
turtle.setheading(0)
skyLine(0)
turtle.penup()
turtle.goto(10, 3.5 * cellSize)
turtle.pendown()

skyLine(0)

turtle.penup()
turtle.goto(0, 4*cellSize - 100)
turtle.pendown()
turtle.color("slate blue")
turtle.pensize(50)
turtle.begin_fill()
turtle.setheading(0)
skyLine(0)


# i=4*cellSize - 150
# while i>0:
#     turtle.penup()
#     turtle.goto(0, i)
#     turtle.pendown()
#     turtle.color("peru")
#     turtle.pensize(100)
#     turtle.begin_fill()
#     turtle.setheading(0)
#     skyLine(0)
#     i=i-10
turtle.penup()
turtle.goto(-2, 3.5 * cellSize)
turtle.pendown()
#Draw the big tree
turtle.color("black")
turtle.pensize(10)
turtle.left(25)
turtle.forward(100)

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

turtle.penup()
turtle.goto(-2, 4 * cellSize)
turtle.pendown()


turtle.color("black")
turtle.pensize(1)
turtle.right(25)
turtle.forward(100)
tree(4)

turtle.penup()
turtle.goto(-2, 4.5 * cellSize)
turtle.pendown()

turtle.color("black")
turtle.pensize(5)
turtle.right(25)
turtle.forward(100)
tree(3)

turtle.penup()
turtle.goto(-2, 3 * cellSize)
turtle.pendown()

turtle.color("black")
turtle.pensize(2)
turtle.left(75)
turtle.forward(100)
tree(3)



for row in range (0,16):
    for col in range(0,16):
        # Move to the lower left corner of the cell.
        turtle.penup()
        turtle.goto(col*cellSize/2+20,row*cellSize/2 +60)
        turtle.pendown()

        # Determine what color should be used based on location in the grid.
        turtle.color("white")

        # Draw a square, filled in.
        turtle.begin_fill()
        turtle.setheading(0)
        for i in range(0,4):
            turtle.forward(1.5)
            turtle.left(90)
        turtle.end_fill()



turtle.penup()
turtle.color("white")
turtle.goto(7.5*cellSize, 0)
turtle.pendown()
turtle.pensize(6)
turtle.begin_fill()
turtle.setheading(0)
turtle.circle(100, 1000)
turtle.end_fill()
i=0
while i<5:
    turtle.penup()
    turtle.color("white")
    turtle.goto(i * cellSize, 0)
    turtle.pendown()
    turtle.pensize(6)
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.circle(100, 1000)
    turtle.end_fill()
    i = i+1
# turtle.right(30)
# def tree(i):
#     if i<10:
#         return
#     else:
#         #turtle.forward(i)
#         turtle.color("black")
#         turtle.right(60)
#         tree(i/2)
#         turtle.forward(i)
# tree(150)
turtle.begin_fill()
turtle.setheading(0)
turtle.end_fill()

screen.mainloop()