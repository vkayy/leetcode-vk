class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return isPalindrome(i + 1, j) or isPalindrome(i, j - 1)
            i += 1
            j -= 1
        return True

# first we have a helper function implementing a palindrome check
# notice that it takes in left and right pointers rather than a string
# maintains O(N) complexity by preventing substring processing
# perform typical two pointers, but in the case of inequality:
# return whether isPalindrome(i + 1, j) or isPalindrome(i, j - 1) holds
# in the case of inequality, increment and decrement as usual
# if no inequality is detected, return true