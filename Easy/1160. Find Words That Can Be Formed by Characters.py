from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            for ch in word:
                if word.count(ch) > chars.count(ch):
                    break
            else:
                res += len(word)
        return res

# for each word in the list of words, we iterate through the chars in the word
# if the count of any char in the word is greater than that of the string, break
# if the for loop is not broken, add the length of the word to the result
# return the result