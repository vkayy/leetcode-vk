class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res

# first, create a set to store the characters
# set the result to zero
# set the left pointer to zero
# iterate through each index as a right pointer

# while the current character is in the set
# remove the left character from the set
# increment the left pointer

# add the current character to the set
# set the result to the max of the result and the length of the substring

# return the result