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
            countCur = Counter()
            
            for k in range(i, i + lenWords, lenWord):
                countCur[s[k: k + lenWord]] += 1
                
            if countCur == countWords:
                result.append(i)
                
            for j in range(i, len(s), lenWord):
                countCur[s[j:j + lenWord]] -= 1
                countCur[s[j + lenWords:j + lenWords + lenWord]] += 1
                
                if countCur == countWords:
                    result.append(j + lenWord)
                    
        return result

# initialise counter for each remainder of dividing by lenWord to get each section
# get initial counter, if it matches append
# slide window across
# return result
