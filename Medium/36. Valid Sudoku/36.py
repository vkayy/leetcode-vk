from typing import List
from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValid(bp: List[List[str]]) -> bool:
            return all(all(v < 2 or k == "." for k, v in Counter(s).items()) for s in bp)
        
        rs = board
        cs = [[r[n] for r in board] for n in range(9)]
        bs = [[board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
              for j in range(0, 9, 3) for i in range(0, 9, 3)]
        
        return isValid(rs + cs + bs)

# we define a function validating a list of rows, columns or boxes
# it returns true if all rows, columns or boxes are valid (the count of each number is less than 2)

# we set rs to the board, as the board is already a list of rows

# we set cs to a list of columns by grouping the nth elements of each row

# we set bs to a list of boxes by grouping the elements of each box
# this is done by iterating through the range of 0 to 9, by 3
# for each iteration, we iterate through the range of 0 to 9, by 3
# for each iteration, we iterate through the range of the current iteration to the current iteration plus 3, for both x and y
# for each iteration, we add the element at the x and y coordinates to the box
# this gets us the in a 3x3 box

# we return the result of isValid with rs, cs, and bs as the parameters 