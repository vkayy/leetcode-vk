from typing import List

class Solution:
  def makeEqual(self, words: List[str]) -> bool:
    joined = ''.join(words)
    letters = set(joined)
    for l in letters:
      if joined.count(l) % len(words):
        return False
    return True

# first, we join all the words together
# this is because we want to find the total number of each letter
# we set letters to a set of joined
# this is because we want to find the unique letters

# then, we iterate through the letters
# if the count of the letter in joined modulo the length of words is not 0
# i.e., the occurrences of that letter can't be distributed evenly
# we return False
# otherwise, we return True