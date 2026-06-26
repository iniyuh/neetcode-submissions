class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hm = {}
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue

                I, J = nums[i], nums[j]
                sum = I + J

                if sum not in hm: hm[sum] = set()

                if (i, j) not in hm[sum] and (j, i) not in hm[sum]:
                    hm[sum].add((i, j) if I <= J else (j, i))
        
        ans = set()
        for k, K in enumerate(nums):
            if -1 * K in hm:
                for (i, j) in hm[-1 * K]:
                    if k == i or k == j: continue

                    I, J = nums[i], nums[j]

                    if K <= I: ans.add((K, I, J))
                    elif K <= J: ans.add((I, K, J))
                    else: ans.add((I, J, K))
        
        return list(ans)