class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        cnt = Counter(num % space for num in nums)
        mxt = cnt.most_common(1)[0][1]
        return min(num for num in nums if cnt[num % space] == mxt)

# first, we count the number of times each modulo appears in nums
# then, we find the most common modulo and its count
# finally, we return the smallest number in nums that has the most common modulo