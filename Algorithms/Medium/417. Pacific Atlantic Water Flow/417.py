from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visited, prev):
            
            visited.add((r, c))
            
            for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (rr, cc) in visited:
                    continue
                if not 0 <= rr < rows or not 0 <= cc < cols:
                    continue
                if heights[rr][cc] < heights[r][c]:
                    continue
                dfs(rr, cc, visited, heights[r][c])
            
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        res = []
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r,c) in atl:
                    res.append([r, c])
        
        return res

# we create visited sets for pacific and atlantic

# then, we create a function called dfs that takes in a row, column, visited, and prev
# we add the row and column to visited

# then, we iterate through the directions
# if the row and column is in visited, we continue
# if the row and column is out of bounds, we continue
# if the height at the row and column is less than the prev, we continue
# we call dfs on the row and column, visited, and the height at the row and column

# then, we iterate through the rows
# we call dfs on the row, 0, pac, and the height at the row and 0
# we call dfs on the row, cols - 1, atl, and the height at the row and cols - 1
# this is because we want to start from the edges where the water can flow to the ocean

# then, we iterate through the columns
# we call dfs on 0, the column, pac, and the height at 0 and the column
# we call dfs on rows - 1, the column, atl, and the height at rows - 1 and the column
# this is because we want to start from the edges where the water can flow to the ocean

# then, we create a list called res

# then, we iterate through the cells
# if the cell is in pacific and atlantic, we append the cell to res

# finally, we return res