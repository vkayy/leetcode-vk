from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        S, P = len(s), len(p)
        countP = Counter(p)
        curCount = Counter(s[:P])
        result = []

        if countP == curCount:
            result.append(0)

        for i in range(S - P):
            curCount[s[i]] -= 1
            curCount[s[i + P]] += 1
            if curCount == countP:
                result.append(i + 1)
        return result

# get the length of p and s
# get the counter of P, and the coutner of the current substring
# if the counters are the same, append the index to result
# iterate through the range S - P
# subtract 1 from the counter of s[i], then add 1 to s[i + P]
# if the counters are equal, append i + 1
# note that we do not append i as s[i] is the char removed