'''
Buatlah sebuah program python dengan pengulangan dan pengkondisian. Jika nilai merupakan kelipatan 3 dan 5, maka output adalah "Fizz Buzz". Jika kelipatan 3, output adalah "Fizz". Jika kelipatan 5, output adalah "Buzz". Selain itu output adalah angka itu sendiri
'''

for i in range(100):
	if i%15==0:
		print('Fizz Buzz')
	elif i%5==0:
		print('Buzz')
	elif i%3==0:
		print('Fizz')
	else:
		print(i)