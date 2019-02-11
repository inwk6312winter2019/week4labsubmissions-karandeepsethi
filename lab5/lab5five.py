class Point():
		"""this is point class"""


		def __init__(self,x=0,y=0):
			self.x=x
			self.y=y
		def __str__(self):
			return "%2d,%2d"% (self.x,self.y)

def add(n1,n2):
	sum=Point()
	sum.x=n2.x+n1.x
	sum.y=n1.y+n2.y
	return sum



n1=Point(2,3)
n2=Point(3,4)
print(add(n1,n2))
