from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        matches = []
        
        def backtrack(i, cur, total):
            
            if total == target:
                matches.append(cur.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            backtrack(i, cur, total + candidates[i])
            
            cur.pop()
            backtrack(i + 1, cur, total)
        
        backtrack(0, [], 0)
        
        return matches

# we set matches to an empty list

# we create a function called backtrack that takes in an index, a current list, and a total
# if the total is equal to the target, we append the current list to matches and return

# if the index is greater than or equal to the length of candidates, or if the total is greater than the target, we return

# we append the element at the index of candidates to cur
# we call backtrack on the index, cur, and total plus the element at the index of candidates

# we pop the last element from cur
# we call backtrack on the index plus 1, cur, and total

# we call backtrack on 0, an empty list, and 0

# finally, we return matches