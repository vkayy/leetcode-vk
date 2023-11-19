class Solution:
    def isAnagram(self, s: str, t: str) -> bool:    
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
    
        # could also do Counter(s) == Counter(t)

# first checks that their lengths are equal
# for each character in the strings
# increment the corresponding value in the dictionary
# default to zero to ensure no errors
# then compare for each dictionary value
# Counter(s) == Counter(t) handles all of this