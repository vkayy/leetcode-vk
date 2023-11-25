from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        slow = 0
        for fast in range(1, len(intervals)):
            if intervals[slow][1] >= intervals[fast][0]:
                intervals[slow][1] = max(intervals[slow][1], intervals[fast][1])
            else:
                slow += 1
                intervals[slow] = intervals[fast]
        return intervals[:slow + 1]

# we sort the intervals by their start times
# we have two pointers, slow and fast
# slow is the pointer for the last merged interval
# fast is the pointer for the next interval to be merged

# we iterate through the intervals starting from the second one

# if the slow interval and the fast interval overlap
# we merge them by updating the end of the slow interval
# we have to take max of the two end times
# this is because the fast interval end may be contained within the slow interval

# if the slow interval and the fast interval do not overlap
# we increment slow and assign the fast interval to slow
# this is because the fast interval is the next interval to be merged

# we return the intervals up to slow + 1