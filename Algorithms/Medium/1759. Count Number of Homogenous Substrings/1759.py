from itertools import groupby

class Solution:
  def countHomogenous(self, s: str) -> int:
    return sum((n := len(list(g))) * (n + 1) // 2 for _, g in groupby(s)) % (10 ** 9 + 7)
  
# the idea is to use the groupby function from itertools
# we iterate through the string
# we use the groupby function to group the characters
# we use a list comprehension to calculate the number of homogenous substrings
# the number of homogenous substrings in a string of repeated characters is given by n * (n + 1) // 2 where n is the length of the substring
