import re
from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return max((self.longestSubstring(sub, k) for sub in re.split('|'.join(leasts), s)), default = 0) if (leasts := [ch for ch, v in Counter(s).items() if v < k]) else len(s)

# the idea is to use a recursive approach to calculate the length of the longest substring with at least k repeating characters
# if the least frequent character has a frequency less than k, we return the length of the longest substring with at least k repeating characters
# otherwise, we return the length of the string
# we use a list comprehension to calculate the least frequent characters
# we use a regular expression to split the string by the least frequent characters
# we use a generator expression to calculate the length of the longest substring with at least k repeating characters
# if the least frequent characters is empty, we return the length of the string
# otherwise, we return the maximum length of the longest substring with at least k repeating characters
# the time complexity is O(N) and the space complexity is O(N)
