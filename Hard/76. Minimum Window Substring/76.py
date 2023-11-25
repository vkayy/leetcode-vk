from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(s) < len(t):
            return ""
        
        minString = ""
        
        countS = Counter()
        countT = Counter(t)
        
        l = 0
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            if countS >= countT:
                while countS >= countT:
                    countS[s[l]] -= 1
                    l += 1
                if minString != "":
                    minString = min(s[l - 1:r + 1], minString, key=len)
                else:
                    minString = s[l - 1:r + 1]
        return minString
            
# first, check if the strings are equal
# if so, return the string
# if the length of s is less than the length of t
# return the empty string

# set the minimum string to the empty string
# create a dictionary to store the count of each character in s
# create a dictionary to store the count of each character in t

# set the left pointer to zero
# iterate through each index as a right pointer
# increment the count of the current character

# if the count of s is greater than or equal to the count of t

# while the count of s is greater than or equal to the count of t
# decrement the count of the left character
# increment the left pointer

# if the minimum string is not the empty string
# set the minimum string to the minimum of the current substring, the minimum string by length
# else, set the minimum string to the current substring

# return the minimum string