from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        lenWord = len(words[0])
        lenWords = len("".join(words))

        curSub = s[:lenWords]
        countWords = Counter(words)
        countCur = Counter([curSub[i:i + lenWord] for i in range(0, len(curSub), lenWord)])
        
        concats = []
        if countWords == countCur:
            concats.append(0)
        
        for i in range(len(s) - lenWords):
            curSub = s[i + 1:i + 1 + lenWords]
            countCur = Counter([curSub[j:j + lenWord] for j in range(0, len(curSub), lenWord)])
            if countCur == countWords:
                concats.append(i + 1)
        return concats

# get the length of a word
# get the length of the whole list per element
# get the first sub
# generate counter for words
# generate coutner for cur by taking first lenWords elements and splitting by every lenWord elements
# set concats to empty
# if the initial counter is equal to countWords, append the index 0
# for i in range (len(s) - lenWords), recalculate the counter
# if they're equal append i + 1