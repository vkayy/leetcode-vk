class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

# first, we filter the string for alphanumeric chars
# this returns an iterable that we join with empty string
# then, we convert this to lower
# use two pointers
# if the two pointers are not equal, then not a palindrome
# if i and j are never unequal, return true