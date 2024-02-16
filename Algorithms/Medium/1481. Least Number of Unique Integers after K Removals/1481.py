from typing import List
from collections import Counter
from itertools import accumulate

class Solution:
  def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    return len([v for v in accumulate(sorted(Counter(arr).values())) if v > k])

# first, we count the frequency of each number in the array
# then we sort the frequency and accumulate the sum of the frequency
# finally, we count the number of unique integers whose frequency is greater than k
# this is because we can remove the numbers with the least frequency first
