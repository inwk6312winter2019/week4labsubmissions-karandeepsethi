class Point():
		"""this is class point"""

def add(self,t):
	sum=Point()
	if t==tuple():
		sum.x=self.x+t[0]
		sum.y=self.y+t[1]
		return sum.x,sum.y
	else:
		sum.x=self.x+t.x
		sum.y=self.y+t.y
		return sum.x,sum.y
n1=Point()
n1.x=2
n1.y=3
n2=Point()
n2.x=3
n2.y=6
print(add(n1,n2))
