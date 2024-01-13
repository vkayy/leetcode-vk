from collections import Counter

class Solution:
  def minSteps(self, s: str, t: str) -> int:
    return (Counter(s) - Counter(t)).total()

# find the difference between the two strings
# the difference is the number of characters that need to be changed