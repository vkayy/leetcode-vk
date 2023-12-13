from typing import List
from functools import reduce

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        return reduce(lambda acc, digit: [perm + new for perm in acc for new in map[digit]], digits, [""]) if digits else []

# maps each digit to its corresponding letters
# if digits is empty, return an empty list

# we can use reduce to iterate through each digit in digits
# we can use the accumulator to keep track of the current permutations
# we can use the current digit to get the corresponding letters
# we can then iterate through each permutation in the accumulator

# for each permutation, we can iterate through each letter
# we can add the letter to the current permutation
# then, we can add the new permutation to the accumulator
# then, we can return the accumulator
# if digits is empty, we can return an empty list