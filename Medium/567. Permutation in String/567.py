from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        sbst = set(s1)
        cnts = Counter(s1)
        cntw = Counter([c for c in s2[:len(s1)] if c in sbst])
        if cnts == cntw:
                return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            if s2[l] in sbst:
                cntw[s2[l]] -= 1
            if s2[r] in sbst:
                cntw[s2[r]] += 1
            if cnts == cntw:
                return True
            l += 1
        return False

# first, we check if the length of s2 is less than the length of s1
# if it is, we return false, as s1 cannot be a substring of s2

# then, we create a set of the characters in s1
# we create a counter of the characters in s1
# we create a counter of the characters in the first len(s1) characters of s2 that are in sbst

# if the counter of s1 is equal to the counter of the first len(s1) characters of s2 that are in sbst, we return true

# we set l to 0
# we iterate through the range of len(s1) to len(s2)
# this is the sliding window technique

# if the character at l is in sbst, we decrement the counter of the character at l
# if the character at r is in sbst, we increment the counter of the character at r
# this effectively shifts the window by one character

# if the counter of s1 is equal to the counter of the characters in the window, we return true

# otherwise, we increment the left pointer

# if we have not returned true, we return false