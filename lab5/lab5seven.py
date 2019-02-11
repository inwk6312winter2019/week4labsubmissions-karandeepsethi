class Kangaroo():
		"""This is the class"""

		def __init__(self):
			self.pouch_contents=[]
		def put_in_pouch(self,val):
			self.pouch_contents.append(val)
		def __str__(self):
			return str(self.pouch_contents)

kanga=Kangaroo()
roo=Kangaroo()
roo.put_in_pouch("kanga's program")
kanga.put_in_pouch(roo)

for i in kanga.pouch_contents:
	print(i)
