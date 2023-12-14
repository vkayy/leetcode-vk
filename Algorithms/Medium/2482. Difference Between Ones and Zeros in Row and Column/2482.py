from typing import List
from itertools import product

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = [], []
        for row in grid:
            rows.append((row.count(1), row.count(0)))
        for col in zip(*grid):
            cols.append((col.count(1), col.count(0)))
        for i, j in product(range(len(grid)), range(len(grid[0]))):
            grid[i][j] = rows[i][0] + cols[j][0] - rows[i][1] - cols[j][1]
        return grid

# first, we count the number of 1s and 0s in each row and column
# then, we use the formula to calculate the difference in each cell
# we return the grid after the calculation