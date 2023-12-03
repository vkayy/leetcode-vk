from typing import List
from collections import defaultdict
from itertools import product

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rs = defaultdict(set)
        cs = defaultdict(set)
        bs = defaultdict(set)
        for r, c in product(range(9), range(9)):
            n = board[r][c]
            if n == ".":
                continue
            if (n in rs[r] or
                n in cs[c] or
                n in bs[r // 3, c // 3]):
                return False
            rs[r].add(n)
            cs[c].add(n)
            bs[r // 3, c // 3].add(n)
        return True

# we initialise a hash map for rows, columns and boxes

# we iterate through the cartesian product of the range of 0 to 9
# this gives us the coordinates of each cell
# we set n to the element at the coordinates

# if n is ".", we continue

# if n is in the hash map for the current row, column or box, we return false
# this is because the number is already in the row, column or box

# if n is not in the hash map for the current row, column or box, we add it to the hash maps

# we return true if we have not returned false