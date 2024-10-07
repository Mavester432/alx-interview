#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's Triangle up to level n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    # Initialize the Pascal's triangle list
    triangle = [[1]]

    for i in range(1, n):
        # Get the previous row
        prev_row = triangle[-1]
        # Create the new row starting and ending with 1
        row = [1]
        # Fill the middle values
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        # Add the new row to the triangle
        triangle.append(row)

    return triangle
