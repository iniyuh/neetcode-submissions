class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def median(nums, l, r):
            if (l + r) % 2 == 0:
                return nums[(l + r) // 2]
            else:
                return ( nums[(l + r) // 2] + nums[(l + r) // 2 + 1] ) / 2

        def combinedMedian(nums1, l1, r1, nums2, l2, r2):
            L1, L2 = r1 - l1 + 1, r2 - l2 + 1

            if (L1 + L2) % 2 == 1: 
                if (L1 + L2) // 2 > L1 - 1:
                    return nums2[l2 + (L1 + L2) // 2 - L1]
                else: return nums1[l1 + (L1 + L2) // 2]
            else:
                right_idx = (L1 + L2) // 2

                if right_idx < L1: return (nums1[l1 + right_idx] + nums1[l1 + right_idx - 1]) / 2
                elif L1 <= right_idx - 1: return (nums2[l2 + right_idx - 1 - L1] + nums2[l2 + right_idx - L1]) / 2
                else: return (nums1[r1] + nums2[l2]) / 2
        
        if not nums1: return median(nums2, 0, len(nums2) - 1)
        if not nums2: return median(nums1, 0, len(nums1) - 1)
        
        l1, r1, l2, r2 = 0, len(nums1) - 1, 0, len(nums2) - 1


        while l1 <= r1 and l2 <= r2:
            if nums1[r1] <= nums2[l2]: return combinedMedian(nums1, l1, r1, nums2, l2, r2)
            elif nums2[r2] <= nums1[l1]: return combinedMedian(nums2, l2, r2, nums1, l1, r1)
            else:
                L1, L2 = r1 - l1 + 1, r2 - l2 + 1
                L = L1 + L2

                if L == 2:
                    return (nums1[l1] + nums2[l2]) / 2
                elif L == 3:
                    if L1 == 1: return nums1[l1]
                    elif L2 == 1: return nums2[l2]
                else:
                    Q = L // 4

                    if Q >= L1:
                        if nums[l1] <= nums[l2] < nums[r1]:
                            return median(nums2, l2 + L1 - Q, r2 - Q)
                        else: 
                            return median(nums2, l2 + Q, r2 - Q + L1)

                    elif Q >= L2:
                        if nums[l1] <= nums[l2] < nums[r1]:
                            return median(nums1, l2 + Q, r1 - Q + L2)
                        else: 
                            return median(nums1, l1 - Q + L2, r1 - Q)
                    else: 
                        if nums1[l1] <= nums2[l2]:
                            l1 += Q
                            r2 -= Q
                        else:
                            l2 += Q
                            r2 -= Q
        
        if l1 > r1: return median(nums2, l2, r2)
        else: return median(nums1, l1, r2)

