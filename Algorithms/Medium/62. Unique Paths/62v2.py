class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1] * n for _ in range(m)]
        
        for i in range(m - 2, -1, -1):
            
            for j in range(n - 2, -1, -1):
                
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        
        return dp[0][0]

# first, we create a 2d list of size m x n filled with 1
# this is because the number of ways to reach the bottom right corner from the bottom right corner is 1

# then, we iterate through the rows backwards
# this is because our recurrence relation depends on the row below the current row

# then, we iterate through the columns backwards
# this is because our recurrence relation depends on the column to the right of the current column

# the paths from a cell is the sum of the paths from the cell below and the cell to the right
# this is because we can only reach the current cell from the cell below or the cell to the right

# finally, we return the number of paths from the top left corner