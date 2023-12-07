from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        time = [(target - p) / s for p, s in cars]
        fleets, lead = 1, time[-1]
        while time:
            if lead < time[-1]:
                fleets += 1
            else:
                time[-1] = lead
            lead = time.pop()
        return fleets
    
# initialise a list of tuples of the position and speed of the cars
# sort in non-decreasing order of position
# initialise a list of the time it takes for each car to reach the target
# initialise the number of fleets to 1
# initialise the lead time to the time it takes for the last car to reach the target

# while the list of times is non-empty

# if lead time is less than the time it takes for the last car to reach the target
# then, we can increment the number of fleets
# this is because the last car will not be able to catch up to the lead car

# otherwise, we can set the time it takes for the last car to reach the target to the lead time
# this is because the last car will be able to catch up to the lead car

# then, we can pop the last time from the list of times

# return the number of fleets