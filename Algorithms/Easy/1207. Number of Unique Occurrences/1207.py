from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
      return len(c := Counter(arr).values()) == len(set(c))

# if the no. of counts is the same as no. of unique counts
