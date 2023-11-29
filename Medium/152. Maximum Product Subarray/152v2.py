from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prevmn, prevmx = 1, 1
        currmn, currmx = nums[0], nums[0]
        
        gmx = float("-inf")
        
        for num in nums:
            
            currmn = min(num, num * prevmn, num * prevmx)
            currmx = max(num, num * prevmn, num * prevmx)
            
            if currmx > gmx:
                gmx = currmx
            
            prevmn = currmn
            prevmx = currmx
            
        return gmx