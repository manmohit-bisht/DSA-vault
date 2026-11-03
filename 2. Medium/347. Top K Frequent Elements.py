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

# More optimal solution in O(N) using bucket sort
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        # initialize a frequency map and a bucket array of size n+1
        freq_map = {}
        bucket_array = [[] for x in range(n+1)]
        ans = []

        #create a frequency table
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        for num,freq in freq_map.items():
            bucket_array[freq].append(num) # bucket[freq] -> list of numbers with that frequency
        
        for i in range(n,-1,-1): # iterate from the end of the bucket array to the start, as we want the most frequent elements
            for j in range(len(bucket_array[i])): 
                ans.append(bucket_array[i][j])
                if len(ans) >= k:
                    return ans
