'''
buatlah sebuah fungsi yang menerima parameter berupa kata dan cek apakah kata itu palindrome atau bukan.
Palindrome adalah susunan kata yang bisa dibaca terbalik.
a. ada -> palindrome
b. kasurusak -> palindrome
c. kuy -> bukan palindrome
'''

def palindrome(kata):
	if kata == kata[::-1]:
		print('palindrome')
	else:
		print('bukan palindrome')
	

palindrome('ada')
palindrome('kasurusak')
palindrome('kuy')