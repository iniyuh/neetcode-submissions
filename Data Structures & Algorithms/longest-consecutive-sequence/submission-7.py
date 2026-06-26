class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        hm = {}

        for num in nums:
            if num in hm: continue

            print("EXECUTING", num)

            if num - 1 in hm and num + 1 in hm:
                start, end = hm[num - 1], hm[num + 1]
                hm[start] = end
                hm[end] = start
                hm[num] = num

                print(start, hm[start])
                print(end, hm[end])

            elif num - 1 in hm:
                hm[num] = hm[num - 1]
                hm[hm[num - 1]] = num
                print(num, hm[num])
                print(num - 1, hm[num - 1])

            elif num + 1 in hm:
                hm[num] = hm[num + 1]
                hm[hm[num + 1]] = num
                print(num, hm[num])
                print(num + 1, hm[num + 1])

            else: hm[num] = num
        
        max_ = 1
        for key, val in hm.items():
            print(key, val)
            max_ = max(max_, abs(key - val) + 1)
        
        return max_
            