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
