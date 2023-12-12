from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n + 1):
            
            if i == offset * 2:
                offset *= 2
            
            dp[i] = 1 + dp[i - offset]
        
        return dp
            
# first, we create a list called dp, filled with 0s
# this is because we want to keep track of the number of 1 bits in each number from 0 to n

# then, we create a variable called offset and set it to 1
# this is because we want to keep track of the offset between the current number and the previous power of 2

# then, we iterate through the numbers from 1 to n

# if i is equal to offset times 2
# i.e., if i is a power of 2
# we set offset to offset times 2

# we set the value at i to 1 plus the value at i minus offset
# this is because the number of 1 bits in i is 1 plus the number of 1 bits in i minus offset

# finally, we return dp