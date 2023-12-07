from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r, k = 1, max(piles), float("inf")
        while l <= r:
            m = (l + r) // 2
            hs = sum(ceil(p / m) for p in piles)
            if h < hs:
                l = m + 1
            else:
                r, k = m - 1, min(k, m)
        return k

# we can use binary search to find the minimum eating speed
# first, the minimum possible eating speed is 1
# the maximum possible eating speed is the maximum number of bananas in a pile

# while l is less than or equal to r
# we set m to be the middle of l and r

# we set hs to be the number of hours needed to eat all the bananas at speed m

# if h is less than hs, i.e., we need more hours than we have
# we set l to be m + 1

# otherwise, we set r to be m - 1
# we set k to be the minimum of k and m

# return k