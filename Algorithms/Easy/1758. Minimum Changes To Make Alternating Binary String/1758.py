class Solution:
  def minOperations(self, s: str) -> int:
    one = 0
    for i, unit in enumerate(s):
      if i % 2:
        if unit == '1':
          one += 1
      else:
        if unit == '0':
          one += 1
    return min(one, len(s) - one)

# first, we initialise the changes to 0
# we check how many changes we need to make if the first unit is 1

# if the first unit is 1, we need to change all the odd indices to 0
# conversely, if the first unit is 1, we need to change all the even indices to 1
# we keep track of the number of changes we need to make in one

# we return the minimum of one and len(s) - one
# this is because we can always flip the string to get the other result
