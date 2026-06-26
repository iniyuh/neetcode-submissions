class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)

        for num in nums: frequency[num] += 1

        bucket = [[] for _ in range(len(nums))]
        for key, val in frequency.items():
            bucket[val - 1].append(key)
        
        i, j = len(bucket) - 1, 0
        ret = []

        while len(ret) != k:
            if bucket[i] and j < len(bucket[i]):
                ret.append(bucket[i][j])
                j += 1
            else:
                j = 0
                i -= 1
                while not bucket[i]: i -= 1
        
        return ret
            

            