'''
1. lakukan pengulangan. hanya print angka genap
2. buat sebuah list atau tuple yang hanya berisi angka ganjil dari range 1 - 100
3. temukan angka yang hilang pada list yang berisi angka 0-20
'''

# for i in range(0,100,2):
# 	print(i)

# listKu = [i for i in range(1,100,2)]
# print(listKu)
listKu = [0,1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20]

print(listKu)

for index, value in enumerate(listKu):
	if not index == value:
		print(index) 
		break