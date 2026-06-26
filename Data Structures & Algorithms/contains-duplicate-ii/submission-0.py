class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = {nums[0]}
        L, R = 0, 1

        while R < len(nums):
            if R - L > k: 
                visited.remove(nums[L])
                L += 1
            
            if nums[R] in visited: return True
            else:
                visited.add(nums[R])
                R += 1
        
        return False
