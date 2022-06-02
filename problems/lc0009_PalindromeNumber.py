def palindrome_number(x: int) -> bool:
	# 数字有偶数位，1221， x是12，reversed_number是12，x == reversed_number
	# 数字有偶数位，12321， x是123，reversed_number是12，x // 10 == reversed_number
	# 以上两种情况，当reversed_number > x时，停下来返回False
	# 需要考虑x是个位数的情况

	if x < 0 or (x % 10 == 0 and x != 0):  # x为负数或末位为0但值不为0时不是回文数
		return False
	reversed_number = 0
	while True:
		if x == reversed_number or x // 10 == reversed_number:
			return True
		elif reversed_number > x:
			return False
		reversed_number = reversed_number * 10 + x % 10
		x = x // 10
