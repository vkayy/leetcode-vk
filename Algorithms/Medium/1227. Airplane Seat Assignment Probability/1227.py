class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 if n == 1 else 0.5

# if there is only one person, then they will always get their seat
# otherwise, the probability of the last person getting their seat is 0.5