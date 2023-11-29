from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        dpmx = [num for num in nums] + [1]
        dpmn = [num for num in nums] + [1]
        
        gmx = float("-inf")
        
        for i, num in enumerate(nums):

            dpmx[i] = max(dpmx[i], num * dpmn[i - 1], num * dpmx[i - 1])
            dpmn[i] = min(dpmn[i], num * dpmn[i - 1], num * dpmx[i - 1])
            
            if dpmx[i] > gmx:
                gmx = dpmx[i]

        return gmx