class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)
        visited = set()
        ret = []
        
        def dfs(currArr):
            if len(currArr) == L: ret.append(currArr)
            else:
                visited.add(currArr[-1])

                for num in nums:
                    if num not in visited: 
                        val = dfs(currArr + [num])
                
                visited.remove(currArr[-1])
        

        for seed in nums:
            dfs([seed])
        
        return ret