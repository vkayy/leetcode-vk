from collections import Counter

class Solution:
  def closeStrings(self, word1: str, word2: str) -> bool:
    count1 = Counter(word1)
    count2 = Counter(word2)
    if count1 == count2:
      return True
    if sorted(count1.keys()) == sorted(count2.keys()):
      return sorted(count1.values()) == sorted(count2.values())
    return False

# first, check if the words are anagrams
# if not, check if the words have the same characters
# if not, return False
# if yes, check if the words have the same number of each character
# if yes, return True
# this means they can be rearranged to be the same