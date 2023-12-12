from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        dpmn, dpmx = [num for num in nums] + [1]
        
        gmx = float("-inf")
        
        for i, num in enumerate(nums):
            
            temps = [dpmx[i], num * dpmn[i - 1], num * dpmx[i - 1]]
            dpmx[i], dpmn[i] = max(temps), min(temps)
            
            gmx = max(gmx, dpmx[i])

        return gmx

# first, we define two lists to store the current minimum and maximum product

# then, we define a variable to store the global maximum product

# then, we iterate through the numbers

# we set temps to the three possible choices for the current product

# we set the current minimum to the minimum of temps
# we set the current maximum to the maximum of temps

# we set the global maximum to the maximum of the current maximum and the global maximum

# finally, we return the global maximum
