#!/usr/bin/env python3
"""
Given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the image by 90 degrees (clockwise).
    args:
        matrix: n x n 2D matrix representing an image.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
