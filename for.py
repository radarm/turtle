import turtle              
wn = turtle.Screen()       
alex = turtle.Turtle() 
n=100
h=5
szog=360/n
for i in range(n):
    alex.forward(h)
    alex.left(szog)
