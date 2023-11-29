from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        currmn, currmx = 1, 1
        
        gmx = float("-inf")
        
        for num in nums:
            
            temps = [num, num * currmn, num * currmx]
            currmn, currmx = min(temps), max(temps)
            
            gmx = max(gmx, currmx)
            
        return gmx