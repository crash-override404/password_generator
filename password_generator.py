#!/usr/bin/env python

import sys

from matrix import matrix


def get_char_from_matrix(x, y):
    return matrix[x][y]


def update_seed_position(seed_length, seed_pos):
    return 0 if seed_pos + 1 == seed_length else seed_pos + 1


def update_salt_position(salt_length, salt_pos):
    return 0 if salt_pos + 1 == salt_length else salt_pos + 1


def generate():
    generated = ""

    # length of seed:
    seed_length = len(seed)
    seed_pos = 0

    # length of salt:
    salt_length = len(salt)
    salt_pos = 0

    for i in range(0, int(length) - 1):
        x = ord(seed[seed_pos]) - 1
        y = ord(salt[salt_pos]) - 1
        generated += get_char_from_matrix(x, y)
        seed_pos = update_seed_position(seed_length, seed_pos)
        salt_pos = update_salt_position(salt_length, salt_pos)

    return generated


if __name__ == "__main__":
    # get seed, salt and password length from ARGS
    seed = sys.argv[1]
    salt = sys.argv[2]
    length = sys.argv[3]

    generated_password = generate()
    print generated_password
