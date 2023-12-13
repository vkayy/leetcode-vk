from typing import List

class Solution(object):
    def numSpecial(self, mat: List[List[int]]):
        cnt = 0
        for i in range(len(mat)):
            if mat[i].count(1) == 1:
                j = mat[i].index(1)
                if [m[j] for m in mat].count(1) == 1:
                    cnt += 1
        return cnt

# initialise count to 0

# iterate through the matrix
# if the number of 1s in the row is 1
# get the index of the 1
# if the number of 1s in the column is 1
# increment count

# return count