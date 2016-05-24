#!/usr/bin/env python
import random


def matrix_generate():
	matrix = {}
	for x in range(48, 122):
		matrix[x] = {}
		for y in range(48, 122):
			matrix[x][y] = chr(random.randint(48, 122))
	return matrix


# print generated matrix
print matrix_generate()
