class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0
        
        for _ in range(32):
            
            res = (res << 1) + (n & 1)
            n >>= 1
                
        return res

# first, we create a variable called res and set it to 0

# then, iterate for each bit in the 32-bit integer

# we shift res left by 1 and add the result of n & 1
# this is because we want to append the least significant bit of n to res

# then, we right shift n by 1, moving to the next bit

# after the loop, we return res