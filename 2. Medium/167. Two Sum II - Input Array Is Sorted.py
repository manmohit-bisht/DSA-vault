class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        i = 0
        j = n - 1

        while i < j:
            sm = numbers[i] + numbers[j]
            if sm == target:
                return [i + 1, j + 1]
            elif sm < target:
                i += 1
            else:
                j -= 1
