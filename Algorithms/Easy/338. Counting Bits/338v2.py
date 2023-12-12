from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp
            
# first, we create a list called dp, filled with 0s

# then, we iterate through the numbers from 1 to n

# we set the value at i to the value at i right shifted 1 plus the value at i bitwise and 1
# the number of 1 bits in i is that of i right shifted 1 plus the least significant bit of i

# this is because if i is even, the number of 1 bits in i is that of i right shifted 1
# but, if i is odd, the number of 1 bits in i is that of i right shifted 1 plus 1

# finally, we return dp