from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(cur, rem):
            if not rem:
                res.append(cur)
                return
            for num in rem:
                backtrack(cur + [num], [n for n in rem if n != num])
        backtrack([], nums)
        return res

# initialise an empty list to store the permutations

# define a backtrack function that takes in a current permutation and a list of remaining numbers
# if there are no remaining numbers, then add the current permutation to the list of permutations
# otherwise, iterate through the remaining numbers
# for each number, add it to the current permutation
