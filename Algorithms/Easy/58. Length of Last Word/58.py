class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

# gets the last word in the string
# returns the length of the last word