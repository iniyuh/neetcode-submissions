class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        ret = set()
        curr = []

        def helper(i, currSum):
            if currSum == target: ret.add(tuple(curr))
            elif currSum > target or i == len(candidates): return
            else:
                curr.append(candidates[i])
                helper(i + 1, currSum + candidates[i])
                curr.pop()

                helper(i + 1, currSum)
        
        helper(0, 0)
        return [list(combination) for combination in ret]