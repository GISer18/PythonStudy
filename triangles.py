#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#杨辉三角
def triangles():
	line = [1]
	yield line
	line = [1, 1]
	yield line
	while True:
		line  = [line[i] + line[i + 1] for i in range(len(line) - 1)]
		line.insert(0, 1)
		line.append(1)
		yield line

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break