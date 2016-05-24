#!/usr/bin/env python

import sys

from matrix import matrix


def main():
	# get seed, salt and password length from ARGS
	seed = sys.argv[1]
	salt = sys.argv[2]
	length = sys.argv[3]

	# length of seed:
	seed_length = len(seed)
	seed_pos = 0

	# length of salt:
	salt_length = len(salt)
	salt_pos = 0

	generated_password = ""
	for i in range(0, int(length) - 1):
		x = ord(seed[seed_pos]) - 1
		y = ord(salt[salt_pos]) - 1
		generated_password += matrix[x][y]
		seed_pos = 0 if seed_pos + 1 == seed_length else seed_pos + 1
		salt_pos = 0 if salt_pos + 1 == salt_length else salt_pos + 1

	print generated_password


main()
