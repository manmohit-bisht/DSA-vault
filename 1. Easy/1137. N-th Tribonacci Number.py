class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            next_value = a + b + c
            a = b
            b = c
            c = next_value
        return c


# Recursive solution (not efficient for large n)


class RecursiveSolution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return (
                self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            )
