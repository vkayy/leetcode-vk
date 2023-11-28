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
        
        m, n = len(board), len(board[0])
        
        if len(word) > m * n: return False                            # [a] trivial case to discard

        if not (cnt := Counter(word)) <= Counter(chain(*board)):      # [b] there are not enough
            return False                                              #     letters on the board
        
        if cnt[word[0]] > cnt[word[-1]]:                              # [c] inverse word if it's better
             word = word[::-1]                                        #     to start from the end
        
        def dfs(i, j, s):                                             # recursive postfix search
            
            if s == len(word) : return True                           # [1] found the word
            
            if 0 <= i < m and 0 <= j < n and board[i][j] == word[s]:  # [2] found a letter
                board[i][j] = "#"                                     # [3] mark as visited
                adj = [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]               # [4] iterate over adjacent cells...
                dp = any(dfs(ii,jj,s+1) for ii,jj in adj)             # [5] ...and try next letter
                board[i][j] = word[s]                                 # [6] remove mark
                return dp                                             # [7] return search result

            return False                                              # [8] this DFS branch failed
                
        return any(dfs(i,j,0) for i,j in product(range(m),range(n)))  # search starting from each position