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

# first, we define two variables to store the current minimum and maximum product

# then, we define a variable to store the global maximum product

# then, we iterate through the numbers

# we set temps to the three possible choices for the current product
# the current number, the current number times the current minimum, and the current number times the current maximum

# we set the current minimum to the minimum of temps
# we set the current maximum to the maximum of temps

# we set the global maximum to the maximum of the current maximum and the global maximum

# finally, we return the global maximum