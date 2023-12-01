class Solution:
    def hammingWeight(self, n: int) -> int:
        
        weight = 0
        
        while n > 0:
            
            weight += n & 1
            n >>= 1

        return weight

# first, we create a variable called weight and set it to 0
# this is because we want to keep track of the number of 1 bits in n

# then, while n is greater than 0

# we increment weight by the result of n & 1
# this is because we want to see if the last bit of n is 1
# if it is, we increment weight by 1

# then, we right shift n by 1
# this is because we want to check the next bit of n

# after the loop, we return weight