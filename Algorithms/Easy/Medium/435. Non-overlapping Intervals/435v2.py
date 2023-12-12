from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[1])
        
        res = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            
            if start < prevEnd:
                res += 1
            else:
                prevEnd = end
        
        return res

# first, we sort the intervals by the end of each interval
# by having the smallest end first, we ensure that the interval overlaps with the fewest intervals

# then, we create variables called res and prevEnd and set them to 0 and the end of the first interval
# these track the number of intervals to remove and the end of the last interval in the result

# then, we iterate through the intervals starting from the second interval

# if the start of the current interval is less than the end of the last interval
# i.e., if the current interval overlaps with the last non-overlapping interval
# we increment res because we want to remove the current interval

# otherwise, the current interval does not overlap with the last non-overlapping interval
# so we set the end of the last interval to the end of the current interval

# after the loop, we return res