from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        lenWord = len(words[0])
        lenWords = len(words) * lenWord
        countWords = Counter(words)
        result = []
        
        for i in range(lenWord):
            left = i
            right = i
            countCur = Counter()
            
            while right + lenWord <= len(s):
                word = s[right:right + lenWord]
                right += lenWord
                countCur[word] += 1
                
                while countCur[word] > countWords[word]:
                    countCur[s[left:left + lenWord]] -= 1
                    left += lenWord
                
                if right - left == lenWords:
                    result.append(left)
        
        return result
    
    # get word length
    # get length of concatenated words
    # get counter of words
    # set result to empty
    
    # for the range of lenWord (to capture all remainders, ie, 0 1 2 for 3)
    # set the starting point of the window to i, and initialise counter
    
    # for each iteration of the while loop, take substring of length lenWord
    # shift the right pointer by lenWord
    # increment the count of this word
    
    # then, for each iteration of the inner while loop, take the word
    # check if the count of that word is greater than the needed words
    # if so, decrement the count of the word on the left by 1
    # shift the left pointer by 1
    
    # after this while loop, the count of that word will be corrected
    # thus, if the distance between right and left is lenWords, this must be valid
    # there can't be any duplicates as at least two words would have invalid count
    