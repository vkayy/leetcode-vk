import random

class RandomizedSet:

  def __init__(self):
    self.rarr = []
    self.imap = {}

  def insert(self, val: int) -> bool:
    if val in self.imap:
      return False
    self.imap[val] = len(self.rarr)
    self.rarr.append(val)
    return True

  def remove(self, val: int) -> bool:
    if val not in self.imap:
      return False
    idx, last = self.imap[val], self.rarr[-1]
    self.rarr[-1], self.rarr[idx] = self.rarr[idx], self.rarr[-1]
    self.imap[last] = self.imap[val]
    self.rarr.pop()
    del self.imap[val]
    return True
      
  def getRandom(self) -> int:
      return self.rarr[random.randrange(0, len(self.imap.items()))]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# to insert, append to the array and add to the map

# to remove, swap the element to be removed with the last element, pop the last element, and remove the element from the map

# to get random, get a random index from the map and return the element at that index
