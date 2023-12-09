from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums2, nums1 = nums1, nums2
        m, n = len(nums1), len(nums2)
        half = (m + n) // 2
        l, r = 0, m - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            lp1 = nums1[i] if i >= 0 else float("-inf")
            rp1 = nums1[i + 1] if i + 1 < m else float("inf")
            lp2 = nums2[j] if j >= 0 else float("-inf")
            rp2 = nums2[j + 1] if j + 1 < n else float("inf")
            if lp1 <= rp2 and lp2 <= rp1:
                if (m + n) % 2:
                    return min(rp1, rp2)
                else:
                    return (max(lp1, lp2) + min(rp1, rp2)) / 2
            elif lp1 > rp2:
                r = i - 1
            else:
                l = i + 1

# set nums1 to be the smaller array
# this is because we use a binary search
# which requires us to know the shorter array
# otherwise, we will get an index out of range error

# set m and n to be the lengths of nums1 and nums2
# set half to be the half of the combined length of nums1 and nums2
# set l and r to be 0 and m - 1
# these are the left and right pointers for nums1
# they enable us to find where to split nums1 and nums2 for the median

# iterate until we find the median

# set i to be the middle of l and r
# set j to be half - i - 2
# this is because we need the total left elements to be half

# set lp1 to be the left element of nums1 at i
# if i is less than 0, set lp1 to be negative infinity
# this handles the case where the left partition only has elements from nums2

# set rp1 to be the right element of nums1 at i + 1
# if i + 1 is greater than or equal to m, set rp1 to be positive infinity
# this handles the case where the right partition only has elements from nums2

# set lp2 to be the left element of nums2 at j
# if j is less than 0, set lp2 to be negative infinity
# this handles the case where the left partition only has elements from nums1

# set rp2 to be the right element of nums2 at j + 1
# if j + 1 is greater than or equal to n, set rp2 to be positive infinity
# this handles the case where the right partition only has elements from nums1

# if lp1 is less than or equal to rp2 and lp2 is less than or equal to rp1
# i.e., if the left partition is less than or equal to the right partition
# the left partition and right partition are valid

# if the combined length of nums1 and nums2 is odd
# return the minimum of rp1 and rp2
# this is because the median is the minimum of the right partition

# if the combined length of nums1 and nums2 is even
# return the average of the maximum of lp1 and lp2 and the minimum of rp1 and rp2
# this is because the median is the average of the maximum of the left partition and the minimum of the right partition

# otherwise, the left partition is greater than the right partition

# if lp1 is greater than rp2
# i.e., if the left partition of nums1 is too big
# set r to be i - 1
# this is because we need to make the left partition smaller

# otherwise, the right partition of nums2 is too big
# set l to be i + 1
# this is because we need to make the left partition bigger