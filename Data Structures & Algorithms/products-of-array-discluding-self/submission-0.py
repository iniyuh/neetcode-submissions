class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = False
        for num in nums: 
            if num != 0: product *= num
            else: 
                if zero: return [0] * len(nums)
                zero = True

        res = []
        for num in nums:
            if num != 0 and not zero: res.append(int(product / num))
            elif num == 0: res.append(product)
            else: res.append(0)

        return res