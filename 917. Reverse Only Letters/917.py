class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1
        
        while i < j:
            while i < j and not s[i].isalpha():
                i += 1
            while i < j and not s[j].isalpha():
                j -= 1
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        return "".join(s)

# first we make s a list as strings are immutable
# typical two pointer method
# skip over values that are not alpha
# swap i and j
# increment and decrement i and j
# return the joined s as a string