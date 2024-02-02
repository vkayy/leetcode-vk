from typing import List

class Solution:
  def sequentialDigits(self, low: int, high: int) -> List[int]:
    # res, cur, n = [], 0, 1
    # d = len(str(low))
    # while True:
    #   if n == 10 - d + 1:
    #     d += 1
    #     n = 1
    #   cur = sum(k * 10 ** i for i, k in enumerate(range(n + d - 1, n - 1, -1)))
    #   n += 1
    #   if cur > high:
    #     break
    #   if cur < low:
    #     continue
    #   res.append(cur)
    # return res

    seq = "123456789"
    res = []
    for i in range(len(seq)):
      for j in range(i + 1, len(seq) + 1):
        if low <= (cur := int(seq[i:j])) <= high:
          res.append(cur)
    return sorted(res)
  
# first solution: enumeration
# first, initialise an empty array for the result
# then, initialise a pointer to the first digit
# then, initialise the number of digits
# then, iterate through the sequence of digits
# if the current number is 10 - d + 1, increment the number of digits and reset the pointer
# then, calculate the current number
# then, increment the pointer
# if the current number is more than high, break
# if the current number is less than low, continue
# otherwise, add the current number to the result
# return the result

# second solution: sliding window
# first, initialise the sequence of digits
# then, initialise an empty array for the result
# then, iterate through the sequence for the left pointer
# then, iterate through the sequence for the right pointer
# if the current number is within the range, add it to the result
# return the sorted result
