from typing import List

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        
        def isUnique(s: List[str]):
            if len(s) == len(set(s)):
                return True
            return False
    
        curSub = list(s[:3])
        count = 0
        if isUnique(curSub):
            count += 1
        
        for i in range(len(s) - 3):
            curSub.pop(0)
            curSub.append(s[i + 3])
            if isUnique(curSub):
                count += 1
        return count

# if the string length is less than subarray length, return 0
# function to check whether a string is unique
# first, take the first current value
# initialise the output value based ont he current value
# for each index in the range of the length minus subarray length
# remove the first index of the current value
# append the i + kth value from the input to the current value
# check the condiiton
# if it holds, add 1