from typing import List
from collections import Counter

class Solution:
  def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    return [sorted(set(list(zip(*matches))[0]) - set(list(zip(*matches))[1])), sorted(p for (p, f) in (Counter(list(zip(*matches))[1]).items()) if f == 1)]

# first, get the set of players who won
# then, take away the set of players who lost
# this is the set of players who have never lost

# then, get all the losers and their frequencies, filtering for one loss
