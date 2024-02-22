class Solution:
  def brokenCalc(self, startValue: int, target: int) -> int:
    res = 0
    while startValue < target:
      target, res = target + 1 if target % 2 else target // 2, res + 1
    return res + startValue - target

# we go from the target to the start value
# if the target is odd, we add 1 to the target
# if the target is even, we divide the target by 2
# it is more efficient to divide first, as any increment prior is an increment of 0.5
