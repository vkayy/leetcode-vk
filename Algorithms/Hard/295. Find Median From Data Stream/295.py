import heapq

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.small, -num)

        if (self.small and self.large and (-self.small[0]) > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
            
        if (S := len(self.small)) > (L := len(self.large)):
            return -self.small[0]
        elif L > S:
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2

# define a class called MedianFinder

# define an __init__ method that takes in self
# set self.small to an empty list
# set self.large to an empty list


# define an addNum method that takes in self and a num
# push -num to self.small

# if self.small and self.large and -self.small[0] is greater than self.large[0]
# set val to -heapq.heappop(self.small)
# push val to self.large
# we negate val because heapq is a min heap, but we want a max heap

# if the length of self.small is greater than the length of self.large plus 1
# set val to -heapq.heappop(self.small)
# push val to self.large

# if the length of self.large is greater than the length of self.small plus 1
# set val to heapq.heappop(self.large)
# push val to self.small


# define a findMedian method that takes in self

# if the length of self.small is greater than the length of self.large
# return -self.small[0]
# this is because we negate the numbers in self.small

# if the length of self.large is greater than the length of self.small
# return self.large[0]
# this is because we don't negate the numbers in self.large

# otherwise, return (-self.small[0] + self.large[0]) / 2
# this is because we want the average of the two middle numbers