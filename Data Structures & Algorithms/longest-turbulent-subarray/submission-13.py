"""
We have an array:
3 5 2 6 | 7 8 9
"""

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1: return len(arr)

        comp = "LT" if arr[0] < arr[1] else "GT"
        maxLength = 1
        currLength = 1

        i = 1

        while i < len(arr):
            if arr[i] == arr[i-1]:
                while i < len(arr) and arr[i] == arr[i-1]: i += 1

                if i == len(arr): break

                currLength = 2
                comp = "LT" if arr[i-1] > arr[i] else "GT"
            elif (comp == "LT" and arr[i-1] < arr[i]) or (comp == "GT" and arr[i-1] > arr[i]):
                currLength += 1
                comp = "LT" if comp == "GT" else "GT"
            else:
                currLength = 2
                comp = "LT" if arr[i-1] > arr[i] else "GT"

            print(arr[i], currLength, comp)
            i += 1
            maxLength = max(maxLength, currLength)
        
        return maxLength