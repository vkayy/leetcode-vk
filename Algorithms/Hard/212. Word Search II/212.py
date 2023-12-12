from typing import List

class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def insert(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.insert(word)
        
        rows, cols = len(board), len(board[0])
        res, visited = set(), set()
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                (r, c) in visited or
                board[r][c] not in node.children):
                return
            
            visited.add((r, c))
            
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord:
                res.add(word)
                
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            
            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        return list(res)

# first, we create a TrieNode class

# then, we create a TrieNode called root
# we iterate through the words
# for each word, we insert it into the TrieNode

# then, we create a set called res
# we create a set called visited

# then, we create a function called dfs
# it takes in r, c, node, and word
# if r or c is out of bounds, or if (r, c) is in visited, or if board[r][c] is not in node.children, we return

# then, we add (r, c) to visited

# then, we traverse to the child of node that corresponds to board[r][c]
# we add board[r][c] to word
# if node.endOfWord is True, we add word to res

# then, we call dfs on r - 1, c, node, and word
# then, we call dfs on r + 1, c, node, and word
# then, we call dfs on r, c - 1, node, and word
# then, we call dfs on r, c + 1, node, and word

# this is to check all the adjacent cells

# then, we remove (r, c) from visited

# in the main function, we iterate through the rows
# then, we iterate through the columns
# then, we call dfs on r, c, root, and ""

# finally, we return res as a list