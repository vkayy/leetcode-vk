from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rs, cs = len(matrix), len(matrix[0])
        l, r = 0, rs * cs - 1
        while l <= r:
            m = (l + r) // 2
            mr, mc = divmod(m, cs)
            if target > matrix[mr][mc]:
                l = m + 1
            elif target < matrix[mr][mc]:
                r = m - 1
            else:
                return True
        return False

# modified binary search
# set rs and cs to be the number of rows and columns in matrix

# set l and r to be 0 and rs * cs - 1

# the pointer for m is the middle of l and r
# set mr and mc to be the row and column of m

# do typical binary search

# return true if target is found
# return false if target is not found