# -*- coding: utf-8 -*-

def is_palindrome(n):
	"""回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数："""
	s0 = str(n)
	for i in range(0, len(s0)/2):
		if s0[i] != s0[-(i+1)]:
			return False
	return True

# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))