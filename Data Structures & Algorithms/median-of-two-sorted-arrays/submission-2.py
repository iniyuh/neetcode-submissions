class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, r1, l2, r2 = 0, len(nums1) - 1, 0, len(nums2) - 1

        def median(arr, l, r):
            if (r - l) % 2 == 0:
                return arr[(l + r) // 2]
            else:
                return (arr[(l + r) // 2] + arr[(l + r) // 2 + 1]) / 2
        
        def medianDuo(a, b, l1, r1, l2, r2):
            # Find k-th (0-based) smallest across a[l1..r1] and b[l2..r2]
            def kth(a, b, l1, r1, l2, r2, k):
                while True:
                    if l1 > r1:  # a is empty
                        return b[l2 + k]
                    if l2 > r2:  # b is empty
                        return a[l1 + k]
                    if k == 0:
                        return a[l1] if a[l1] <= b[l2] else b[l2]

                    n1 = r1 - l1 + 1
                    n2 = r2 - l2 + 1
                    # take i from a and j from b so i + j = k+1
                    i = min(n1, (k + 1) // 2)
                    j = (k + 1) - i
                    ai = a[l1 + i - 1]
                    bj = b[l2 + j - 1]

                    if ai <= bj:
                        l1 += i
                        k -= i
                    else:
                        l2 += j
                        k -= j

            n1 = r1 - l1 + 1
            n2 = r2 - l2 + 1
            L = n1 + n2

            if L % 2 == 1:
                return kth(a, b, l1, r1, l2, r2, L // 2)
            else:
                left = kth(a, b, l1, r1, l2, r2, L // 2 - 1)
                right = kth(a, b, l1, r1, l2, r2, L // 2)
                return (left + right) / 2

        while l1 <= r1 and l2 <= r2:
            # disjoint by value
            if nums1[r1] <= nums2[l2]:
                return medianDuo(nums1, nums2, l1, r1, l2, r2)
            elif nums2[r2] <= nums1[l1]:
                return medianDuo(nums2, nums1, l2, r2, l1, r1)

            # interleaving cases by value
            elif nums1[l1] <= nums2[l2] <= nums1[r1] <= nums2[r2]:
                LENGTH1, LENGTH2 = r1 - l1 + 1, r2 - l2 + 1
                q = (LENGTH1 + LENGTH2) // 4

                # NEW: prevent zero-trim infinite loop
                if q == 0:
                    return medianDuo(nums1, nums2, l1, r1, l2, r2)

                if q < LENGTH1 and q < LENGTH2:
                    l1 += q
                    r2 -= q
                elif LENGTH1 <= q:
                    diff = q - LENGTH1
                    return median(nums2, l2 + diff, r2 - q)
                else:
                    diff = q - LENGTH2
                    return median(nums1, l1 + q, r1 - diff)

            else:
                LENGTH1, LENGTH2 = r1 - l1 + 1, r2 - l2 + 1
                q = (LENGTH1 + LENGTH2) // 4

                # NEW: prevent zero-trim infinite loop
                if q == 0:
                    return medianDuo(nums1, nums2, l1, r1, l2, r2)

                if q < LENGTH1 and q < LENGTH2:
                    l2 += q
                    r1 -= q
                elif LENGTH1 <= q:
                    diff = q - LENGTH1
                    return median(nums2, l2 + q, r2 - diff)
                else:
                    diff = q - LENGTH2
                    return median(nums1, l1 + diff, r1 - q)

        # Fallback if one range collapses—compute directly
        return medianDuo(nums1, nums2, max(l1, 0), max(r1, -1), max(l2, 0), max(r2, -1))