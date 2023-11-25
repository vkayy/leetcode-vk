from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(s) < len(t):
            return ""
        
        countS = Counter()
        countT = Counter(t)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        
        l = 0
        
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""

# first, check if the strings are equal
# if so, return the string
# if the length of s is less than the length of t
# return the empty string

# create a dictionary to store the count of each character in s
# create a dictionary to store the count of each character in t

# set the have to zero
# set the need to the length of t
# set the result to [-1, -1]
# set the result length to infinity

# set the left pointer to zero
# iterate through each index as a right pointer
# increment the count of the current character

# if the current character is in the dictionary
# and the count of the current character is equal in both dictionaries
# increment the have

# while the have is equal to the need
# if the length of the current substring is less than the result length
# set the result to the current substring
# set the result length to the length of the current substring
# decrement the count of the left character
# if the left character is in the dictionary
# and the count of the left character is less in the dictionary
# decrement the have
# increment the left pointer

# return the result if the result length is not infinity
# else, return the empty string