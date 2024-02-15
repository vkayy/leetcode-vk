from functools import lru_cache

class Solution:
  def numDistinct(self, s: str, t: str) -> int:
    m, n = len(s), len(t)
    @lru_cache(None)
    def dp(i, j):
      if j == n:
        return 1
      if i == m or (m - i < n - j):
        return 0
      return dp(i + 1, j) + (dp(i + 1, j + 1) if s[i] == t[j] else 0)
    return dp(0, 0)

# we use dynamic programming to solve this problem
# we create a recursive function to calculate the number of distinct subsequences
# we use memoization to optimize the recursive function

# if the pointer for the string t reaches the end, we return 1
# this is because we have found a distinct subsequence

# if the pointer for the string s reaches the end, we return 0
# this is because we have reached the end of the string s without finding a distinct subsequence

# if the remaining length of the string s is less than the remaining length of the string t, we return 0
# this is because we cannot find a distinct subsequence with the remaining characters in the string s

# if the current characters of the strings s and t are different, we call the recursive function with the next character of the string s
# this is to see whether we can find a distinct subsequence with the remaining characters in the string s

# if the current characters of the strings s and t are the same, we call the recursive function with the next character of the strings s and t
# this is to see whether we can find a distinct subsequence with the remaining characters in the strings s and t
