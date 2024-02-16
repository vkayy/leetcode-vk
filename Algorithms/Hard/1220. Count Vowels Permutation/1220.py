class Solution:
  def countVowelPermutation(self, n: int) -> int:
    a, e, i, o, u, md = 1, 1, 1, 1, 1, 10 ** 9 + 7
    for _ in range(2, n + 1):
      aa = (e + i + u) % md
      ee = (a + i) % md
      ii = (e + o) % md
      oo = i % md
      uu = (i + o) % md
      a, e, i, o, u = aa, ee, ii, oo, uu
    return (a + e + i + o + u) % md

# first, we initialise the counts of each vowel and the modulo
# we know that at a length of 1, each vowel ending has 1 permutation
# therefore, we initialise the counts of each vowel to 1

# then we iterate through the range from 2 to n
# this is because we want the count at a length of n

# at each step, we update the count of each vowel
# an a can follow an e, i, or u
# therefore, the count of a is the sum of the counts of e, i, and u
# similarly, we update the counts of e, i, o, and u

# finally, we return the sum of the counts of each vowel with the modulo
# we add all the counts as these are all the n-length permutations
