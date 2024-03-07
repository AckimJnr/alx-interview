#!/usr/bin/python3
"""
Draws the pascals triangle in lists
"""


def pascal_triangle(n):
    """
    n: number where pascals triangle will be from
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_line = triangle[-1]
        new_line = [1]

        for j in range(1, i):
            new_line.append(prev_line[j - 1] + prev_line[j])

        new_line.append(1)
        triangle.append(new_line)
    return triangle
