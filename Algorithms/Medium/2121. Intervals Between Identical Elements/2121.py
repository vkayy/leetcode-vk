from typing import List
from collections import defaultdict

class Solution:
  def getDistances(self, arr: List[int]) -> List[int]:
    total, count = defaultdict(int), defaultdict(int)
    for i, n in enumerate(arr):
      total[n] += i
      count[n] += 1
    print(total, count)
    return [total[n] - i * count[n] for i, n in enumerate(arr)]
