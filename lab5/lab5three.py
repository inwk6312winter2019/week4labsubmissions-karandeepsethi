class Time(object):

	"""this will tell the time"""

t=Time()
t.hour=10
t.minutes=20
t.seconds=30

def print_time(t):

	print("%.2d:%.2d:%.2d" % (t.hour,t.minutes,t.seconds))

print_time(t)
