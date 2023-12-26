class Solution:
  def numRollsToTarget(self, n: int, k: int, target: int) -> int:
    if n * k < target or target == 0:
      return 0
    
    dp = [[0 for _ in range(n * k + 1)] for _ in range(n + 1)]
    dp[0][target] = 1
    
    for i in range(0, n + 1):
      for j in range(target, -1, -1):
        dp[i][j] += sum(dp[i - 1][j + x] for x in range(1, k + 1) if j + x <= target)
        
    return dp[n][0] % (10 ** 9 + 7)

# first, we check if n * k is less than target or target is 0
# if this is the case, we return 0

# next, we create a 2d array called dp
# dp[i][j] stores the number of ways to get a sum of target starting at j with i dice
# to get to target with 0 dice, we need to start at target

# then, we iterate through i from 0 to n + 1
# we iterate through j from target to 0
# we do this because our recurrence relation depends on the values at i - 1 and j + x
# we iterate through x from 1 to k + 1
# we do this because we can only roll from 1 to k

# we set the value at dp[i][j] to the sum of dp[i - 1][j + x] for x in range(1, k + 1) if j + x <= target
# this is because we can get to j by rolling x and then getting to j + x with i - 1 dice
# we only do this if j + x is less than or equal to target
# this is because we cannot roll more than target

# finally, we return dp[n][0] % (10 ** 9 + 7)
# we do this because dp[n][0] is the number of ways to get a sum of target with n dice