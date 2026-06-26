class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        ret = set()

        def helper(n, curr):
            if n == len(nums): ret.add(tuple(curr))
            else:
                for i in range(len(nums)):
                    if i not in visited:
                        visited.add(i)
                        curr.append(nums[i])
                        helper(n + 1, curr)
                        curr.pop()
                        visited.remove(i)
        
        helper(0, [])
        return list(ret)