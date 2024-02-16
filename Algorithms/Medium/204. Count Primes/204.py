class Solution:
  def countPrimes(self, n: int) -> int:
    if n < 3:
      return 0
    dp = [1] * n
    dp[0], dp[1] = 0, 0
    for i in range(2, int(n ** 0.5) + 1):
      if dp[i]:
        for j in range(i * i, n, i):
          dp[j] = 0
    return sum(dp)

# this is the sieve of eratosthenes algorithm
# we initialise the sieve with 1s
# then we mark the multiples of each prime as 0
# finally, we return the sum of the sieve
# this is because the sieve contains 1s at the prime indices
# therefore, the sum of the sieve is the count of primes

# the reason we set i * i as the start of the inner loop is because all the multiples of i less than i * i have already been marked
# this is because the multiples of i less than i * i are multiples of a smaller prime
