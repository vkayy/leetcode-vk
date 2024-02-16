class Solution:
  def longestPalindromeSubseq(self, s: str) -> int:
    s1, s2 = s, s[::-1]
    l1 = l2 = len(s1)
    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
    for i in range(l1 - 1, -1, -1):
      for j in range(l2 - 1, -1, -1):
        if s1[i] == s2[j]:
          dp[i][j] = 1 + dp[i + 1][j + 1]
        else:
          dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]

# first, we reverse the string
# then we initialise the length of the string
# then we initialise the dp table which has the length of the string + 1
# the dp table represents the length of the longest palindromic subsequence starting from i in s1 and j in s2

# then we iterate through the strings from the end
# if the characters are the same, we add 1 to the length of the longest palindromic subsequence
# we then move to the next characters in the strings
# if the characters are different, we take the maximum length of the longest palindromic subsequence
# we then move to the next character in either strings

# we return the length of the longest palindromic subsequence starting from the first characters of the strings
