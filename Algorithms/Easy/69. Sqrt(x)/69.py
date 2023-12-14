from math import ceil

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, ceil(x / 2)
        while True:
            m = (l + r) // 2
            if m * m <= x < (m + 1) * (m + 1):
                return m
            elif m * m > x:
                r = m - 1
            else:
                l = m + 1

# search for greatest integer m such that m * m <= x < (m + 1) * (m + 1)