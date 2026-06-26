class Solution:
    def helper(self, nums: List[int], set_: Set[List[int]]) -> None:
        set_.add(tuple(nums))

        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i+1:], set_)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        set_ = set()
        self.helper(nums, set_)

        ret = list()
        for i in set_: ret.append(list(i))
        return ret