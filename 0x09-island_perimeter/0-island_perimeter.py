#!/usr/bin/python3
"""
Module: island_perimeter
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island within the grid.

    Args:
        grid (List[List[int]]): The grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # If current cell is land
                perimeter += 4  # Assume it's surrounded by water
                # Check adjacent cells
                if row > 0 and grid[row - 1][col] == 1:  # Up
                    perimeter -= 1
                if row < rows - 1 and grid[row + 1][col] == 1:  # Down
                    perimeter -= 1
                if col > 0 and grid[row][col - 1] == 1:  # Left
                    perimeter -= 1
                if col < cols - 1 and grid[row][col + 1] == 1:  # Right
                    perimeter -= 1

    return perimeter
