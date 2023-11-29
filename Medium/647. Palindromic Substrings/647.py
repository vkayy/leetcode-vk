class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        
        for i in range(len(s)):
            
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res

# first, we create a variable called res and set it to 0

# then, we iterate through the string

# we set l and r to i
# l will be the left pointer and r will be the right pointer
# this covers the case where the palindrome is odd in length

# while the pointers are in bounds and the characters at the pointers are equal
# we increment res by 1
# we decrement l and increment r
# this is to expand the substring

# we repeat, but this time, we set l to i and r to i + 1
# this covers the case where the palindrome is even in length

# then, we return res