class Solution:
    def climbStairs(self, n: int) -> int:
        
        prev, curr = 1, 1
        
        for i in range(n - 1):
            prev, curr = curr, prev + curr
        
        return curr

# we set prev and curr to 1

# then, we iterate through n - 1
# we set prev to curr and curr to prev plus curr
# this is because we can either take 1 step or 2 steps

# finally, we return curr

# this is dynamic programming because we are using the previous results to calculate the current result