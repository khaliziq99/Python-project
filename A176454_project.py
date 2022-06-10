#Project
#if you want to run a code, just put hashtag beside (""")
#if you want to run next code, remove hashtag on (""") of current code
#Example
"""
import turtle             # Allows us to use turtles
scr = turtle.Screen()      # Creates a playground for turtles
jane= turtle.Turtle()     # Create a turtle, assign to jane
jane.forward(50)          # Tell jane to move forward by 50 units
jane.left(90)             # Tell jane to turn by 90 degrees
jane.forward(30)          # Complete the second side of a rectangle
scr.mainloop()             # Wait for user to close window 
#"""

#Part 1
"""
import turtle
def main():
    shape=str(input("Enter the shape you want:\n")) #enter shape that only inside the python lib
    make_window(shape)
    make_turtle(shape)
    
def make_window(s="arrow"): #arrow as a default shape
    w=turtle.Screen         #create screen
    turtle.title(s)         #create title at the top of windows
    turtle.bgcolor('white') #change background colour
    turtle.screensize(800,600) #change screen size
    

def make_turtle(s="arrow"):
    j= turtle.Turtle() #j as turtle
    j.shape(s)         #call shape from python lib according to the input
    j.color('black')   #shape colour is black
    j.pensize(1)       #set pen size to 1
main()                 #call main method
#"""

#Part 2
#No 4
"""
import turtle
def main():
    shape=str(input("Enter the shape you want (triangle):\n"))
    if shape=='triangle':      #if input equal triangle, do those method
        make_window(shape)
        make_triangle()        #method to create triaangle
    else:
        print("Invalid input") #not inside recommendation
    
def make_window(s="arrow"):
    w=turtle.Screen
    turtle.title(s)
    turtle.bgcolor('white')
    turtle.screensize(800,600)
    

def make_triangle():           #because this method is default triangle
    j= turtle.Turtle()
    j.color('black')
    j.pensize(1)
    j.forward(90)
    j.right(120)
    j.forward(90)
    j.right(120)
    j.forward(90)
    j.right(120)
main()
#make_triangle()
#"""

#No 5
"""
import turtle
def main():
    shape=str(input("Enter the shape you want (triangle,star):\n"))
    if shape=='triangle':      #if input equal triangle, do those method
        make_window(shape)
        make_triangle()        #method to create triaangle
    elif shape=='star':        #if input equal triangle, do those method
        make_window(shape)
        make_star()            #method to create star
    else:
        print("Invalid input") #not inside recommendation
    
def make_window(s="arrow"):
    w=turtle.Screen
    #turtle.title('circle')
    turtle.title(s)
    turtle.bgcolor('white')
    turtle.screensize(800,600)

def make_triangle():           #because this method is default triangle
    j= turtle.Turtle()
    j.color('black')
    j.pensize(1)
    j.forward(90)
    j.right(120)
    j.forward(90)
    j.right(120)
    j.forward(90)
    j.right(120) 

def make_star():               #because this method is default star
    j= turtle.Turtle()
    j.color('black')
    j.pensize(1)
    j.forward(150)             #cannot use loop
    j.right(144)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)

main()
#make_star()
#"""
#No 6
"""
import turtle
def main():
    shape=str(input("Enter the shape you want (triangle,star,multicolour star):\n"))
    if shape=='triangle':
        make_window(shape)
        make_triangle()
    elif shape=='star':
        make_window(shape)
        make_star()
    elif shape=='multicolour star':
        make_window(shape)
        make_multicolourstar()
    else:
        print("Invalid input") #not inside recommendation
    
def make_window(s="arrow"):
    w=turtle.Screen
    #turtle.title('circle')
    turtle.title(s)
    turtle.bgcolor('white')
    turtle.screensize(800,600)

def make_triangle():
    j= turtle.Turtle()
    #j.shape('circle')
    #j.shape(s)
    j.color('black')
    j.pensize(1)
    j.forward(90)
    j.right(120)
    j.forward(90)
    j.right(120)
    j.forward(90)
    j.right(120)    

def make_star():
    j= turtle.Turtle()
    #j.shape('circle')
    #j.shape(s)
    j.color('black')
    j.pensize(1)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)    

def make_multicolourstar():
    j= turtle.Turtle()
    j.color('black')
    j.pensize(1)
    for i in range(5):
        if i==1:
            j.color('blue')
        elif i==2:
            j.color('yellow')
        elif i==3:
            j.color('green')
        elif i==4:
            j.color('red')
        j.forward(150)
        j.right(144)
    j.right(144)
main()
#make_multicolourstar()
#"""

#No 7
"""
import turtle
def main():
    shape=str(input("Enter the shape you want (triangle,star,multicolour star,spiral):\n"))
    if shape=='triangle':
        make_window(shape)
        make_triangle()
    elif shape=='star':
        make_window(shape)
        make_star()
    elif shape=='multicolour star':
        make_window(shape)
        make_multicolourstar()
    elif shape=='spiral':
        make_window(shape)
        make_spiral()
    else:
        print("Invalid input") #not inside recommendation
    
def make_window(s="arrow"):
    w=turtle.Screen
    #turtle.title('circle')
    turtle.title(s)
    turtle.bgcolor('white')
    turtle.screensize(800,600)

def make_triangle():
    j= turtle.Turtle()
    #j.shape('circle')
    #j.shape(s)
    j.color('black')
    j.pensize(1)
    j.forward(90)
    j.right(120)
    j.forward(90)
    j.right(120)
    j.forward(90)
    j.right(120)    

def make_star():
    j= turtle.Turtle()
    #j.shape('circle')
    #j.shape(s)
    j.color('black')
    j.pensize(1)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)    

def make_multicolourstar():
    j= turtle.Turtle()
    #j.shape('circle')
    #j.shape(s)
    j.color('black')
    j.pensize(1)
    j.forward(150)
    j.color('blue')
    j.right(144)
    j.forward(150)
    j.color('yellow')
    j.right(144)
    j.forward(150)
    j.color('green')
    j.right(144)
    j.forward(150)
    j.color('red')
    j.right(144)
    j.forward(150)
    j.right(144)

def make_spiral():
    j= turtle.Turtle()
    j.color('black')
    j.pensize(1)
    for i in range (100):
        j.forward(10+i)
        j.right(20)
    
#main()
#make_spiral()
#"""

#No 8
"""
import turtle
def main():
    shape=str(input("Enter the shape you want (triangle,star,multicolour star,spiral,dotted spiral):\n"))
    if shape=='triangle':
        make_window(shape)
        make_triangle()
    elif shape=='star':
        make_window(shape)
        make_star()
    elif shape=='multicolour star':
        make_window(shape)
        make_multicolourstar()
    elif shape=='spiral':
        make_window(shape)
        make_spiral()
    elif shape=='dotted spiral':
        make_window(shape)
        make_dottedspiral()
    else:
        print("Invalid input") #not inside recommendation
    
def make_window(s="arrow"):
    w=turtle.Screen
    #turtle.title('circle')
    turtle.title(s)
    turtle.bgcolor('white')
    turtle.screensize(800,600)

def make_triangle():
    j= turtle.Turtle()
    #j.shape('circle')
    #j.shape(s)
    j.color('black')
    j.pensize(1)
    j.forward(90)
    j.right(120)
    j.forward(90)
    j.right(120)
    j.forward(90)
    j.right(120)    

def make_star():
    j= turtle.Turtle()
    #j.shape('circle')
    #j.shape(s)
    j.color('black')
    j.pensize(1)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)    

def make_multicolourstar():
    j= turtle.Turtle()
    #j.shape('circle')
    #j.shape(s)
    j.color('black')
    j.pensize(1)
    j.forward(150)
    j.color('blue')
    j.right(144)
    j.forward(150)
    j.color('yellow')
    j.right(144)
    j.forward(150)
    j.color('green')
    j.right(144)
    j.forward(150)
    j.color('red')
    j.right(144)
    j.forward(150)
    j.right(144)

def make_spiral():
    j= turtle.Turtle()
    j.color('black')
    j.pensize(1)
    for i in range (100):
        j.forward(10+i)
        j.right(20)

def make_dottedspiral():
    j= turtle.Turtle()
    j.pensize(1)
    for i in range (100):
        if i%2!=0:
            j.color('black')
            j.forward(10+i)
            j.right(20)
        elif i%2==0:
            j.color('white')
            j.forward(10+i)
            j.right(20)
    
main()
#make_dottedspiral()
#"""

#No 9
"""
import turtle
def main():
    shape=str(input("Enter the shape you want (triangle,star,multicolour star,spiral,dotted spiral,snowflake):\n"))
    if shape=='triangle':
        make_window(shape)
        make_triangle()
    elif shape=='star':
        make_window(shape)
        make_star()
    elif shape=='multicolour star':
        make_window(shape)
        make_multicolourstar()
    elif shape=='spiral':
        make_window(shape)
        make_spiral()
    elif shape=='dotted spiral':
        make_window(shape)
        make_dottedspiral()
    elif shape=='snowflake':
        make_window(shape)
        make_snowflake()
    else:
        print("Invalid input") #not inside recommendation
    
def make_window(s="arrow"):
    w=turtle.Screen
    turtle.title(s)
    turtle.bgcolor('white')
    turtle.screensize(800,600)

def make_triangle():
    j= turtle.Turtle()
    j.color('black')
    j.pensize(1)
    j.forward(90)
    j.right(120)
    j.forward(90)
    j.right(120)
    j.forward(90)
    j.right(120)    

def make_star():
    j= turtle.Turtle()
    j.color('black')
    j.pensize(1)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)
    j.forward(150)
    j.right(144)    

def make_multicolourstar():
    j= turtle.Turtle()
    j.color('black')
    j.pensize(1)
    j.forward(150)
    j.color('blue')
    j.right(144)
    j.forward(150)
    j.color('yellow')
    j.right(144)
    j.forward(150)
    j.color('green')
    j.right(144)
    j.forward(150)
    j.color('red')
    j.right(144)
    j.forward(150)
    j.right(144)

def make_spiral():
    j= turtle.Turtle()
    j.color('black')
    j.pensize(1)
    for i in range (100):
        j.forward(10+i)
        j.right(20)

def make_dottedspiral():
    j= turtle.Turtle()
    j.pensize(1)
    for i in range (100):
        if i%2!=0:
            j.color('black')
            j.forward(10+i)
            j.right(20)
        elif i%2==0:
            j.color('white')
            j.forward(10+i)
            j.right(20)

def make_snowflake():
    j= turtle.Turtle()
    j.color('black')
    j.pensize(1)
    j.speed(0)
    l1=1
    for p in range(6):
        if p==5:
            j.right(36)
        elif p!=5:
            for n in range(6):
                if n==5:
                    j.right(36)
                    j.forward(l2)
                    j.forward(l3)
                    j.forward(l4)
                    l5=l4*3
                    j.forward(l5)
                    j.left(108)
                    j.forward(l5)
                    j.forward(l4)
                    j.forward(l3)
                    j.forward(l2)
                    j.right(144)
                elif n!=5:
                    for m in range(6):
                        if m==5:
                            j.right(36)
                            j.forward(l2)
                            j.forward(l3)
                            l4=l3*3
                            j.forward(l4)
                            j.left(108)
                            j.forward(l4)
                            j.forward(l3)
                            j.forward(l2)
                            j.right(144)
                        elif m!=5:
                            for k in range(6):
                                if k==5:
                                    j.right(36)
                                    j.forward(l2)
                                    l3=l2*3
                                    j.forward(l3)
                                    j.left(108)
                                    j.forward(l3)
                                    j.forward(l2)
                                    j.right(144)
                                elif k!=5:
                                    for i in range(6):
                                        if i==5:
                                            j.right(36)
                                            l2=l1*3
                                            j.forward(l2)
                                            j.left(108)
                                            j.forward(l2)
                                            j.right(144)
                                        elif i!=5:
                                            j.forward(l1)
                                            j.backward(l1)
                                            j.right(72)

main()
#make_snowflake()
#"""
