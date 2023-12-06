class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        mx, l, lst = 0, 0, 0
        
        for r in range(0, len(s)):
            if s[r] == s[r - 1]:
                l = lst
                lst = r
            mx = max(mx, r - l + 1)
        return max(mx, r - l + 1)

# first, initialise the max, left pointer, and last to 0
# the lst variable is the index of the second character of the last repeated pair

# if the current char is the same as the previous char, shift left pointer to lst
# this is so that the following substrings are semi-repetitive

# then, set lst to the current char's index
# this is because the current char is the second char of the last repeated pair

# then, set mx to the maximum of mx and the current length
# this is because we want the longest semi-repetitive substring

# then, return the maximum of mx and the current length
# we must do this as the last character may be the second character of the last repeated pair