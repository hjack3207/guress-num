import random
r = random.randint(1, 100)
while True:
	num = print('請輸入數字1-100')
	num = int(num)
	if num == r:
		print('恭喜猜中數字了')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案大小')
