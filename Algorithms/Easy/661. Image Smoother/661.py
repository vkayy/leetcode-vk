import math
from typing import List
from itertools import product

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        smooth = [[0 for _ in range(n)] for _ in range(m)]
        for i, j in product(range(m), range(n)):
            cnt, cur = 1, img[i][j]
            adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for k, l in adj:
                if 0 <= (i + k) < m and 0 <= (j + l) < n:
                    cnt += 1
                    cur += img[i + k][j + l]
            smooth[i][j] = math.floor(cur / cnt)
        return smooth

# first, initialise an empty list to store the smoothed image
# then, iterate through the image
# for each pixel, initialise a counter and a current sum
# then, iterate through the adjacent pixels
# if the adjacent pixel is valid, increment the counter and add the value to the current sum
# then, add the current sum divided by the counter to the smoothed image
# finally, return the smoothed image