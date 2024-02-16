from itertools import permutations

class Solution:
  def numTilePossibilities(self, tiles: str) -> int:
    pos = set()
    for i in range(len(tiles)):
      for p in permutations(tiles, i + 1):
        pos.add(p)
    return len(pos)

# first, we initialize an empty set to store the unique permutations
# then we generate all the permutations of the tiles
# finally, we return the number of unique permutations
# this is because the set stores only the unique permutations
# therefore, the length of the set is the number of unique permutations
