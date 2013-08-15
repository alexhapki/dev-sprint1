# This is where Exercise 5.4 goes
# Name: Alex Choi

from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()
bob.delay = 0.0001

#1
def koch(t, x):		#t is the turtle's name, x is the length
	if x < 3:
		fd(t, x)
		return		#I can't figure out why the koch curve doesn't draw if I don't have this "return" in the code. Isn't the fd command enough to stop the function?
	koch(t, x/3)
	lt(t, 60)
	koch(t, x/3)
	rt(t, 120)
	koch(t, x/3)
	lt(t, 60)
	koch(t, x/3)

#2
def snowflake(t, x):
	for i in range(3):
		koch(t, x)
		rt(t, 120)	#120 degrees because 360/3 koch curves.



snowflake(bob, 100)


wait_for_user()