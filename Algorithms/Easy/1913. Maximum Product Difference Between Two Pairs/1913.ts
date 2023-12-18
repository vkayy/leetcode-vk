function maxProductDifference(nums: number[]): number {
  let mx1 = 0, mx2 = 0
  let mn1 = Infinity, mn2 = Infinity
  for (var num of nums) {
      if (num > mx1) {
          mx2 = mx1
          mx1 = num
      } else {
          mx2 = Math.max(mx2, num)
      }
      if (num < mn1) {
          mn2 = mn1
          mn1 = num
      } else {
          mn2 = Math.min(mn2, num)
      }
  }
  return mx1 * mx2 - mn1 * mn2
};

// initialise the max and min values
// loop through the array
// if curr is greater than max, set max to curr and set second max to max
// otherwise, set second max to max of curr and second max
// if curr is less than min, set min to curr and set second min to min
// otherwise, set second min to min of curr and second min