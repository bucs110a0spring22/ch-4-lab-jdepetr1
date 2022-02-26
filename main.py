import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help


def setupWindow(screen_object):
  '''
  Sets up the region the turtle screen is to focus on
  screen_object: (Screen) screen object

  return: None
  '''
  screen_object.setworldcoordinates(-360, -1, 360, 1)
  screen_object.bgcolor("white")

def setupAxis(turtle_object):
  '''
  Draws x and y axes of graph on turtle screen
  turtle_object: (Turtle) turtle object

  return: None
  '''
  turtle_object.up()
  turtle_object.goto(0,0)
  turtle_object.color("Black")
  turtle_object.down()

  turtle_object.goto(380,0)
  turtle_object.goto(-380,0)
  turtle_object.goto(0,0)
  turtle_object.goto(0,-2)
  turtle_object.goto(0,2)

def drawSineCurve(turtle_object):
  '''
  Draws a sine curve on turtle screen from [-360, 360]
  turtle_object: (Turtle) turtle object

  return: None
  '''
  turtle_object.up()
  turtle_object.goto(-360,0)
  turtle_object.color("red")
  turtle_object.down()

  for degree in range(-360,361):
    turtle_object.goto(degree, math.sin(math.radians(degree)))

def drawCosineCurve(turtle_object):
  '''
  Draws a cosine curve on turtle screen from [-360, 360]
  turtle_object: (Turtle) turtle object

  return: None
  '''
  turtle_object.up()
  turtle_object.goto(-360,1)
  turtle_object.color("blue")
  turtle_object.down()

  for degree in range(-360,361):
    turtle_object.goto(degree, math.cos(math.radians(degree)))

def drawTangentCurve(turtle_object):
  '''
  Draws a tangent curve on turtle screen from [-360, 360]
  turtle_object: (Turtle) turtle object

  return: None
  '''
  turtle_object.up()
  turtle_object.goto(-360,0)
  turtle_object.color("green")
  turtle_object.down()

  for degree in range(-360,361):
    turtle_object.goto(degree, math.tan(math.radians(degree)))





##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)
    
    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
    
main()
