class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xffffffff
        
        while (b & mask) != 0:
            s, c = a ^ b, (a & b) << 1
            a = s
            b = c
        
        return a & mask if b > 0 else a

# here we create a mask of 32 1s
# this is to prevent overflow

# we use a while loop to check if the mask of b is not 0
# if it is not 0, we use the xor operator to get the sum of a and b
# we use the and operator to get the carry of a and b
# we assign the sum to a and the carry to b
# we repeat this process until the carry is 0

# we return the sum of a and b if b is greater than 0
# otherwise, we return a
# this is because if b is greater than 0, then a is positive
# if b is less than 0, then a is negative