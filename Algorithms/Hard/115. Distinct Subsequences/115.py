class Solution:
  def numDistinct(self, s: str, t: str) -> int:
    l1, l2 = len(s), len(t)
    dp = [[int(not j) for j in range(l2 + 1)] for _ in range(l1 + 1)]
    for i in range(1, l1 + 1):
      for j in range(1, l2 + 1):
        dp[i][j] = dp[i - 1][j]
        if s[i - 1] == t[j - 1]:
          dp[i][j] += dp[i - 1][j - 1]
    return dp[l1][l2]

# here, we use a 2D array to store the number of distinct subsequences
# we initialize the first row and column with 1s
# we iterate through the 2D array
# we calculate the number of distinct subsequences for each cell
# we return the result
