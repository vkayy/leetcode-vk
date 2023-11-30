from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = gmx = nums[-1]
        
        for num in reversed(nums[:-1]):
            
            curr = max(num, num + curr)
            gmx = max(gmx, curr)
        
        return gmx

# first, we create variables curr and gmx and set them to the last number in nums
# this is because the maximum subarray ending at the last index is the number at that index

# then, we iterate through the numbers backwards

# we set curr to the maximum of the number and the number plus curr
# this is because the maximum subarray starting at i is either that number or it plus the maximum subarray starting at i + 1

# we set gmx to the maximum of gmx and curr
# this is because the maximum subarray is either the current maximum subarray or the current maximum subarray ending at i

# finally, we return gmx

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = gmx = nums[-1]
        
        for num in reversed(nums[:-1]):
            
            if num + curr > num:
                curr = num + curr
            else:
                curr = num

            if curr > gmx:
                gmx = curr
        
        return gmx

# this is the same as the above solution, except we use if statements instead of max
# this is because we want to avoid using the max function
# this is because the max function is slower than if statements