class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        H, N = len(haystack), len(needle)
        if N > H:
            return -1

        for i in range(H - N + 1):
            if haystack[i] == needle[0]:
                if haystack[i:i + N] == needle:
                    return i
        return -1

# if there is no needle, then it occurs at 0
# otherwise, take length of haystack and needle
# if the needle length is greater than haystack's it is not here
# we subtract N from H and add 1 
# as only at the index before this can needle exist
# if haystack[i] matches the first index of needle
# check to see if whole stirng matches
# if it does, return i
# otherwise, return -1