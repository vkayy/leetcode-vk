from typing import List
from collections import deque
from itertools import product

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "#"
            
            while queue:
                
                r, c = queue.popleft()
                
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    rr, cc = r + dr, c + dc
                    if (0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == "1"):
                        queue.append((rr, cc))
                        grid[rr][cc] = "#"
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        
        return islands

# first, we create a variable called islands and set it to 0

# then, we create a function called bfs that takes in a row and column
# we create a queue
# we add the row and column to the queue
# we set the character at the row and column to "#"
# this is to mark that we have visited this cell

# while the queue is not empty

# we pop the row and column from the queue

# then, we iterate through the directions

# we set rr and cc to the row and column plus the direction
# if rr and cc are in bounds and the character at rr and cc is equal to "1"
# we add rr and cc to the queue
# we set the character at rr and cc to "#"
# this is to mark that we have visited this cell

# then, we iterate through the grid
# if the character at the row and column is equal to "1"
# we increment islands by 1
# we call bfs on the row and column

# essentially, once we find a "1", we increment islands by 1
# then, we mark all the cells that are connected to this cell as visited