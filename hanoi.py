#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# steps = []
formatStr = 'move %s from %s to %s'

#把编号1--n个盘子从a柱经过b柱移到c柱
def move(n, a, b, c):
	if n == 1:
		steps.append(formatStr % (n, a, c))
		return
	move(n-1, a, c, b)
	steps.append(formatStr % (n, a, c))
	move(n-1, b, a, c)

for i in range(1,6):
	steps = []
	move (i, 'A', 'B', 'C')
	print('\n%d 个盘子共需要移动%s次，步骤：' % (i, len(steps)))
	for s in steps:
		print(s)

