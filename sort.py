# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	"""将列表按名字排序"""
   	return str.lower(t[0])

def by_score(t):
    """将列表按分数排序"""
    return t[1]

#Test
L2 = sorted(L, key=by_name)
print(L2)

L2 = sorted(L, key=by_score, reverse=True)
print(L2)