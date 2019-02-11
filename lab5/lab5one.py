import math


class Point(object):
	"""this is class for point"""

point_a = Point()
point_b = Point()

point_a.x, point_a.y = 2.0, 2.0
point_b.x, point_b.y = 5.0, 3.0


def distance(point_a, point_b):

    axisx = point_b.x - point_a.x
    axisy = point_b.y - point_a.y
    return math.sqrt(axisx ** 2 + axisy ** 2)

print(distance(point_a,point_b))

