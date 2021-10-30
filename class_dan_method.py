'''
1. membuat class
2. apa itu method?
3. magic method
'''


class Manusia:
	def __init__(self, name, age):
		self.name=name
		self.age=age

	def intro(self):
		return 'nama saya adalah '+ self.name+ ' saya berumur '+ str(self.age)

udin = Manusia('udin', 20)
print(udin.intro())