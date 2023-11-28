from typing import List
from collections import Counter
from itertools import chain, product

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        res = False
        
        def dfs(row, col, index):
            nonlocal res
            if index == len(word):
                res = True
                return
            
            if (row < 0 or col < 0 or
                row == rows or col == cols or
                (row, col) in visited or
                board[row][col] != word[index]):
                return

            visited.add((row, col))
            index += 1

            dfs(row - 1, col, index)
            dfs(row + 1, col, index)
            dfs(row, col - 1, index)
            dfs(row, col + 1, index)

            visited.remove((row, col))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    dfs(r, c, 0)
        
        return res

# first, we create a set called visited
# we create a boolean called res and set it to False

# then, we create a function called dfs that takes in a row, column, and index
# we set res to True if index is equal to the length of word

# if the row or column is out of bounds, or if the row and column is in visited,
# or if the character at the row and column is not equal to the character at the index of word, we return

# we add the row and column to visited
# we increment index by 1

# we call dfs on the row - 1, column, and index
# we call dfs on the row + 1, column, and index
# we call dfs on the row, column - 1, and index
# we call dfs on the row, column + 1, and index

# we remove the row and column from visited

# then, we iterate through the board
# if the character at the row and column is equal to the character at the 0th index of word,
# we call dfs on the row, column, and 0

# finally, we return res

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rs, cs = len(board), len(board[0])
        
        if len(word) > rs * cs:
            return False
        
        if not (count := Counter(word)) <= Counter(chain(*board)):
            return False
        
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (0 <= r < rs and 0 <= c < cs and board[r][c] == word[i]):
                board[r][c] = "#"
                adj = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
                dp = any(dfs(rr, cc, i + 1) for rr, cc in adj)
                board[r][c] = word[i]
                return dp
            return False
        
        return any(dfs(r, c, 0) for r, c in product(range(rs), range(cs)))

# first, we create a variable called rs and set it to the length of board
# we create a variable called cs and set it to the length of board[0]

# we check if the length of word is greater than rs * cs
# i.e., if the length of word is greater than the number of cells in board
# if so, we return False

# we create a variable called count and set it to the Counter of word
# we check if count is less than or equal to the Counter of chain(*board)
# i.e., we check if the characters in word are in board
# if not, we return False

# we check if the count of the first char is greater than that of the last char
# if so, we reverse word

# then, we create a function called dfs that takes in a row, column, and index
# if the index is equal to the length of word, we return True

# if the row and col are in bounds and the char at the row and column is the char at index,
# we set the char at the row and column to "#"
# this is to mark that we have visited this cell
# we create a list called adj that contains the adjacent cells
# we create a boolean called dp and set it to the result of any(dfs(rr, cc, i + 1) for rr, cc in adj)
# i.e., we call dfs on the adjacent cells (dynamic programming)
# we set the char at the row and column to the char at index
# this is to reset the cell
# we return dp

# otherwise, we return False

# then, we return the result of any(dfs(r, c, 0) for r, c in product(range(rs), range(cs)))
# i.e., we call dfs on all the cells in board