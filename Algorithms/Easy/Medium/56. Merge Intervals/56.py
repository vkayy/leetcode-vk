from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])
        
        index = 0
        
        for i in range(1, len(intervals)):
            
            if intervals[index][1] < intervals[i][0]:
                intervals[index + 1] = intervals[i]
                index += 1
            else:
                intervals[index][1] = max(intervals[index][1], intervals[i][1]) 
        
        return intervals[:index + 1]

# we sort the intervals by the start of each interval

# then, we create a variable called index and set it to 0
# this is because we want to keep track of the last interval in the result

# then, we iterate through the intervals starting from the second interval
# this is because we want to compare each interval to the previous interval

# if the end of the last interval is less than the start of the current interval
# i.e., if the current interval is after the last interval
# we set the interval after the last interval to the current interval
# and increment index

# otherwise, the current interval overlaps with the last interval
# more specifically, the end of the last interval is greater than or equal to the start of the current interval
# so we update the end of the last interval to be the maximum of the two ends
# we know the start is less than or equal to the start of the current interval because we sorted the intervals

# after the loop, we return the intervals up to index + 1
# this is because index is the index of the last interval in the result