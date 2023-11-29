from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        ans = [nums[0]]
        
        for num in nums[1:]:
            
            if num > ans[-1]:
                ans.append(num)
                
            else:
                
                l, r = 0, len(ans) - 1
                while l < r:
                    m = (l + r) // 2
                    if num > ans[m]:
                        l = m + 1
                    else:
                        r = m
                        
                ans[l] = num
        
        return len(ans)

# first, we create a list called ans with the first number in nums
# the first subequence we encounter is the first number in nums

# then, we iterate through the numbers in nums from the second number onwards

# if the number is greater than the last number in ans
# we append the number to ans

# otherwise, we perform a binary search on ans to find the first number greater than or equal to the number
# a longer subsequence can be made by replacing the number with the new number
# this is because the new number is smaller than the number it replaced, so it can be used to make a longer subsequence

# note that when num is less than or equal to the number at m, we set r to m
# this is because m could be the number we are looking for, as the condition is greater than or equal to

# when l is equal to r, we have found the number greater than or equal to the number

# finally, we return the length of ans