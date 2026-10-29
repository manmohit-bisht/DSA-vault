class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        nums = [2, 3, 5]
        for i in nums:
            while n % i == 0:
                n //= i
                # we simply divide n by [2,3,5] iteratively until n is no longer divisible by them, this way we can check if n is only made up of these prime factors because if it is, we will eventually reduce n to 1. If n has any other prime factor, it will not be reduced to 1.

        return n == 1
