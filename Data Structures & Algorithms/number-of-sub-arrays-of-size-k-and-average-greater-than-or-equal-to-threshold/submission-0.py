class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        currSum = 0
        ret = 0

        while i < len(arr):
            currSum += arr[i]

            if i > k - 1: currSum -= arr[i - k]
            if i >= k - 1 and currSum / k >= threshold: ret += 1

            i += 1
        
        return ret
