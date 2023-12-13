class WordNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = WordNode()
            curr = curr.children[ch]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                ch = word[i]
                if ch == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                elif ch not in curr.children:
                    return False
                else:
                    curr = curr.children[ch]
            return curr.endOfWord
        
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# for adding words,
# we set curr to root
# then we iterate through the word
# if the character is not in the children of curr, we add it
# then we set curr to the child
# once we reach the end of the word, we set endOfWord to True

# for searching words,
# we use dfs
# we set curr to root
# then we iterate through the word
# if the character is a dot, we iterate through all the children of curr
# if dfs returns True, we return True
# otherwise, we return False
# if the character is not in the children of curr, we return False
# otherwise, we set curr to the child
# once we reach the end of the word, we return curr.endOfWord