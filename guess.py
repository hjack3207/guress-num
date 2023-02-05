import random
r = random.randint(1, 100)
count = 0
while True:
	count = count + 1
	num = print('請輸入數字1-100')
	num = int(num)
	if num == r:
		print('恭喜猜中數字了')
		print('這是你猜的第', count, '次')	
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案大小')
	print('這是你猜的第', count, '次')	
