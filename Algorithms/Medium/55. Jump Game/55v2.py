from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        last = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            
            if last - i <= nums[i]:
                last = i
        
        return last == 0

# first, we create a variable called last and set it to the last index in nums
# this is because we want to see if we can reach the last index from the first index

# then, we iterate through the numbers backwards

# if the distance from the last index to i is less than or equal to the number at i
# i.e., if we can reach the last index from i
# we set last to i

# finally, we return whether last is 0
# i.e., whether we can reach the last index from the first index