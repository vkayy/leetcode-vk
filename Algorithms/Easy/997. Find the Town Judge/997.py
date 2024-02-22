from typing import List
from collections import defaultdict

class Solution:
  def findJudge(self, n: int, trust: List[List[int]]) -> int:
    t = defaultdict(int)
    for a, b in trust:
      t[a] -= 1
      t[b] += 1
    return next((i for i in range(1, n + 1) if t[i] == n - 1), -1)

# we use a defaultdict to store the trust count of each person
# we iterate through the trust list
# we decrement the trust count of the person who trusts
# we increment the trust count of the person who is trusted
