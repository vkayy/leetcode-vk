from typing import List
from collections import Counter
from itertools import chain, product

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def findWord(word):
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
        
        return set(filter(findWord, [word for word in words]))