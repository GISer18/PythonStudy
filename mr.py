# -*- coding: utf-8 -*-

from functools import reduce

#传入字符串，传出首字母大写
def normalize(name):
    return name.capitalize()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#乘积计算
def prod(L):
	return reduce(lambda x, y: x*y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 字符串转换浮点数
def str2float(s):
	intPart = s[0:s.index('.')]
	fracPart = s[-1:s.index('.'):-1]
	print(intPart,fracPart)
	return reduce(lambda x, y: x*10 + y, list(map(int,intPart))) + reduce(lambda x, y: x/10 + y, list(map(int,fracPart)))/10

# Test
print('str2float(\'123.456\') =', str2float('123.456'))
print('str2float(\'123.4\') =', str2float('123.4'))
