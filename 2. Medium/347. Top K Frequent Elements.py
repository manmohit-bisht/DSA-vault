# The solution in O(Nlong(N))

# fmt: off
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_dict = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1

        arr = []
        for key, value in freq_dict.items():
            arr.append((-value, key)) #the value is inserted in negative to sort in descending order
        arr.sort() #if we don't negate the value, we will have to sort in reverse order, i.e. arr.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(arr[i][1])
        return res
