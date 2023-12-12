from typing import List

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        cnt = dec = 0
        for per in batteryPercentages:
            if per - dec <= 0:
                continue
            cnt += 1
            dec += 1
        return cnt

# first we can create a counter and a decrementer

# then, we can iterate through the array
# if the current battery percentage minus the decrementer is less than or equal to zero, we can continue
# this is because we can only test the device if the battery percentage is greater than the decrementer

# otherwise, we can increment the counter and the decrementer
# this is because we have tested the device and the decrementer is incremented by one

# then, we can return the counter