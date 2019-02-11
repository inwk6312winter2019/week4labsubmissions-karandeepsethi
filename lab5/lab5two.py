import math

class Rectangle(object):

	"""this class is for rectangle """

thing = Rectangle()
thing.height=2.0
thing.width=3.0

class Point(object):

	"""this class is for point"""

thing.corner=Point()
thing.corner.x=0.0
thing.corner.y=0.0


def find_center(thing):
	p = thing
	p.x=thing.corner.x+thing.width/2.0
	p.y=thing.corner.y+thing.height/2.0
	return p

corner=find_center(thing)
print(corner.x,corner.y)



def move_rectangle(thing,dx,dy):
	thing.width +=dx
	thing.height +=dy
	return thing.width,thing.height
print(move_rectangle(thing,50,100))


def move_rectangle2(thing):
	import copy
	thing2=copy.copy(thing)
	return thing2
print(move_rectangle2(thing))
