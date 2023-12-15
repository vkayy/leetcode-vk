from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return ({d for _, d in paths} - {s for s, _ in paths}).pop()

# returns the destination city that is not the starting city for any path