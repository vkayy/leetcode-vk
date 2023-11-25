from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

# first, we create a set of the numbers in nums
# then, we iterate through nums

# for each number, we check if the number before it is in the set
# if it is not, then we know that this number is the start of a sequence
# so, we set the length to 1

# while the next number is in the set
# we increment the length

# we update the longest length if the current length is longer
# return the longest length