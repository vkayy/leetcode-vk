from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        
        for i, interval in enumerate(intervals):
            
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            elif newInterval[0] > interval[1]:
                res.append(interval)
            
            else:
                newInterval = [min(newInterval[0], interval[0]),
                               max(newInterval[1], interval[1])]
        
        res.append(newInterval)
        
        return res

# first, we create a list to store the result

# then, we iterate through the intervals

# if the end of the new interval is less than the start of the current interval
# i.e., if the new interval is before the current interval
# we append the new interval to the result
# and return the result plus the rest of the intervals
# this is because we know that the new interval will not overlap with the rest of the intervals

# if the start of the new interval is greater than the end of the current interval
# i.e., if the new interval is after the current interval
# we append the current interval to the result
# we do not append the new interval because we do not know if it will overlap with the rest of the intervals

# otherwise, the new interval overlaps with the current interval
# so we update the new interval to be the union of the two intervals

# after the loop, we append the new interval to the result
# this is because we know that the new interval will not overlap with the rest of the intervals

# finally, we return the result