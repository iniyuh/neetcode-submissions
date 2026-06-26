class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroIndex = -1
        product = 1

        for i, num in enumerate(nums): 
            if num != 0: product *= num
            elif zeroIndex != -1: return [0] * len(nums)
            else: 
                zeroIndex = i
                print(i)
        
        if zeroIndex != -1: 
            ret = [0] * len(nums)
            ret[zeroIndex] = product
            return ret
        else:
            ret = []
            for num in nums: ret.append(int(product / num))
            return ret