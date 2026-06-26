class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        present = set()

        i = 0

        while i < len(nums):
            if i > k: present.remove(nums[i-k-1])

            if nums[i] in present: return True
            else: 
                present.add(nums[i])
                i += 1
        
        return False