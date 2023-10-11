#!/usr/bin/python3
"""Pascal Triangle function."""


def pascal_triangle(n):
    """Pascal Triangle of size n.

    returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    pas_triangles = [[1]]
    while len(pas_triangles) != n:
        pas_tri = pas_triangles[-1]
        temp_tri = [1]
        for i in range(len(pas_tri) - 1):
            temp_tri.append(pas_tri[i] + pas_tri[i + 1])
        temp_tri.append(1)
        pas_triangles.append(temp_tri)

    return pas_triangles
