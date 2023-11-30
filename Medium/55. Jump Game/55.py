from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [False] * (len(nums) - 1) + [True]
        
        for i in range(len(nums) - 2, -1, -1):
            
            for j in range(1, nums[i] + 1):
                
                if i + j < len(nums) and dp[i + j]:
                    dp[i] = True
                    break
                           
        return dp[0] 

# first, we create a list called dp, filled with False except for the last index, which is True
# this is because we can reach the last index from the last index

# then, we iterate through the numbers backwards
# this is because our recurrence relation depends on the numbers to the right of the current number

# then, we iterate through the numbers from 1 to the number at i plus 1
# this is because we can jump from i to i + nums[i]

# if i + j is less than the length of nums and the value at i + j is True
# that is, if we can reach the last index from i + j and i + j is within the bounds of nums

# we set the value at i to True
# this is because we can reach the last index from i
# we break because we only need to find one way to reach the last index from i

# finally, we return the value at 0
# this is because the value at 0 is whether we can reach the last index from the first index