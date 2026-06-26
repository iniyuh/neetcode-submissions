class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1: return len(arr)

        lessThan = True if arr[0] < arr[1] else False
        currLength = 1
        maxLength = 1

        for i in range(1, len(arr)):
            if (lessThan and arr[i-1] < arr[i]) or (not lessThan and arr[i-1] > arr[i]):
                currLength += 1
                maxLength = max(maxLength, currLength)
                lessThan = not lessThan
                print(arr[i-1], arr[i], currLength)
            elif arr[i-1] == arr[i]:
                currLength = 1
                if i+1 < len(arr): lessThan = arr[i] < arr[i+1]
            else:
                currLength = 2
        
        return maxLength
