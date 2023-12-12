from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, map = [], {
            '': [],
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        def backtrack(curr, rem):
            nonlocal res
            if not rem:
                res.append(curr)
                return
            for ch in map[rem[0]]:
                backtrack(curr + ch, rem[1:])
        backtrack("", digits)
        return res if digits else []

# maps each digit to its corresponding letters

# we can use backtracking to generate all possible permutations
# we can use a helper function to perform the backtracking
# we can use the current permutation and the remaining digits as parameters
# if there are no remaining digits, we can add the current permutation to the result
# then, we can return
# otherwise, we can iterate through each letter corresponding to the first digit
# we can add the letter to the current permutation

# then, we can recursively call backtrack with the new permutation and the remaining digits

# then, we can return the result if digits is not empty