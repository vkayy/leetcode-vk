from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            
            for j in range(i + 1, len(nums)):
                
                if nums[i] < nums[j]:
                
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)

# first, we create a list of size len(nums) filled with 1
# this is because the longest increasing subsequence of a single number is 1

# then, we iterate through the numbers backwards
# this is because our recurrence relation depends on the subsequence ending at i

# then, we iterate through the numbers after i
# this is because we are trying to find the longest subsequence starting at i
# we can only do this if the number at i is less than the number at j

# if the number at i is less than the number at j
# set the lis of i to the maximum of the lis of i and the lis of j plus 1
# this is because we can add the number at i to the subsequence ending at j to make a longer subsequence ending at i

# finally, we return the maximum lis