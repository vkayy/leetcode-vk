from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robHelper(nums):
            
            rob1, rob2 = 0, 0

            for num in nums:
                rob0 = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = rob0

            return rob2
        
        return max(nums[0], robHelper(nums[:-1]), robHelper(nums[1:]))

# first, we define a function called robHelper that takes in a list of houses
# this function will return the maximum amount of money we can rob from the houses
# we will use this function twice, once for the first house, and once for the last house
# this is because we cannot rob the first and last houses at the same time

# finally, we return the maximum of the two robHelper calls and the first house
# this covers the case where there is only one house