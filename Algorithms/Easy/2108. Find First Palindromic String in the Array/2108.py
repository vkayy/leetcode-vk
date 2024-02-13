from typing import List

class Solution:
  def firstPalindrome(self, words: List[str]) -> str:
    return ws[0] if (ws := [w for w in words if w == w[::-1]]) else ""

# this takes advantage of lazy evaluation
# finds the first palindrome in the list of words
# or, if there are no palindromes, returns an empty string
