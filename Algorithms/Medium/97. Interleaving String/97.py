from functools import lru_cache

class Solution:
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    l1, l2, l3 = len(s1), len(s2), len(s3)
    @lru_cache(None)
    def dp(p1, p2, p3):
      for i in range(p3, l3):
        if p1 < l1 and p2 < l2 and s3[i] == s1[p1] and s3[i] == s2[p2]:
          return dp(p1 + 1, p2, p3 + 1) or dp(p1, p2 + 1, p3 + 1)
        if p1 < l1 and s3[i] == s1[p1]:
          return dp(p1 + 1, p2, p3 + 1)
        elif p2 < l2 and s3[i] == s2[p2]:
          return dp(p1, p2 + 1, p3 + 1)
        else:
          return False
      return p1 == l1 and p2 == l2
    return dp(0, 0, 0)

# first, create a helper function to use memoization
# we use the pointer method to iterate through the strings
# if the current character is the same for both strings and the third string, we call the helper function twice
# if the current character is the same for the first string and the third string, we call the helper function once
# if the current character is the same for the second string and the third string, we call the helper function once
# if the current character is different for all three strings, we return False
# if we reach the end of the third string, we return True if we also reach the end of the first and second strings
# we call the helper function with the initial pointers
# return the result
