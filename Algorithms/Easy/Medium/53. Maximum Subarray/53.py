from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [num for num in nums]
        
        for i in range(len(nums) - 2, -1, -1):
            
            dp[i] = max(dp[i], nums[i] + dp[i + 1])
        
        return max(dp)

# first, we create a list called dp, filled with the numbers in nums
# this is because the maximum subarray ending at each index is the number at that index

# then, we iterate through the numbers backwards

# we set the value at i to the maximum of the value at i and the value at i plus 1
# this is because the maximum subarray starting at i is either that number or it plus the maximum subarray starting at i + 1

# finally, we return the maximum of dp