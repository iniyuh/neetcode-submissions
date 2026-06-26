class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        ret = []

        def helper(n, curr):
            if n == len(nums): ret.append(curr.copy())
            else:
                for num in nums:
                    if num not in visited:
                        visited.add(num)
                        curr.append(num)
                        helper(n + 1, curr)
                        curr.pop()
                        visited.remove(num)
        
        helper(0, [])

        return ret
