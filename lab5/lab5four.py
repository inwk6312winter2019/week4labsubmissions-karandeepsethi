class Time(object):

	"""this is time class"""

t1 = Time()
t1.hour = 11
t1.minute = 59
t1.second = 30
 
t2 = Time()
t2.hour = 10
t2.minute = 54
t2.second = 22
 
def is_after(t1, t2):
    t1_total_seconds = (t1.hour) + (t1.minute) + (t1.second)
    t2_total_seconds = (t2.hour) + (t2.minute) + (t2.second)
    return t1_total_seconds > t2_total_seconds
     
print (is_after(t1, t2))
