from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
 
    def get(self, key: str, timestamp: int) -> str:
        tvs, res = self.map[key], ""
        l, r = 0, len(tvs) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamp >= tvs[m][0]:
                res = tvs[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
      
# constructor method:  
# set a map to be a defaultdict of lists

# set method:
# append a tuple of timestamp and value to the list in the map at key

# get method:
# set tvs to be the list in the map at key
# set res to be an empty string

# modified binary search (greatest element less than or equal to target)
# if the timestamp is greater than or equal to the timestamp at the middle of tvs
# etc..

# return res