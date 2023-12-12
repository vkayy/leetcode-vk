from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordKey = "$"
        
        root = {}
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node[wordKey] = word
        
        rows, cols = len(board), len(board[0])
        matches = []
        
        def dfs(r, c, parent):
            
            ch = board[r][c]
            board[r][c] = "#"
            
            child = parent[ch]
            
            if word := child.pop(wordKey, False):
                matches.append(word)
            
            for rr, cc in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]:
                if not 0 <= rr < rows or not 0 <= cc < cols:
                    continue
                if not board[rr][cc] in child:
                    continue
                dfs(rr, cc, child)
            
            board[r][c] = ch
            
            if not child:
                parent.pop(ch)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root:
                    dfs(r, c, root)
        
        return matches

# first we create a variable called wordKey and set it to "$"

# then, we create the root of the trie
# we iterate through the words
# for each word, we set node to root
# then, we iterate through the characters in the word
# if the character is not in node, we add it
# then, we set node to the child
# then, we set the wordKey of the node to the word

# then, we create a list called matches

# then, we create a function called dfs that takes in a row, column, and parent

# we set ch to the character at the row and column
# we set the character at the row and column to "#"
# this marks the character as visited

# we set the child node to the traversal of parent at ch

# if the child node has a wordKey, we append the word to matches

# then, we iterate through the adjacent cells
# if the adjacent cell is out of bounds, we continue
# if the adjacent cell is not in the child node, we continue
# otherwise, we call dfs on the adjacent cell, child node, and child

# we set the character at the row and column to ch

# if the child node is empty, we remove the child node from the parent
# it would be empty if no words have the prefix of the characters in the trie
# this is due to the fact that we removed the wordKey of the child node
# optimises by pruning the trie and thus the search space

# then, we iterate through the board
# if the current character is in the root, we call dfs on the row, column, and root

# finally, we return matches