from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        res = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            
            if start >= prevEnd:
                prevEnd = end
            else:
                if end < prevEnd:
                    prevEnd = end
                res += 1
            
        return res

# first, we sort the intervals by the start of each interval
# this is because we want to compare each interval to the previous interval

# then, we create variables called res and prevEnd and set them to 0 and the end of the first interval
# this is because we want to keep track of the number of intervals to remove and the end of the last interval in the result

# then, we iterate through the intervals starting from the second interval

# if the start of the current interval is greater than or equal to the end of the last interval
# i.e., if the current interval is after the last interval
# we set the end of the last interval to the end of the current interval

# otherwise, the current interval overlaps with the last interval

# if the end of the current interval is less than the end of the last interval
# i.e., if the current interval is before the last interval
# we set the end of the last interval to the end of the current interval

# we increment res because we want to remove the current interval

# after the loop, we return res