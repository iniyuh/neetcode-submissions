class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target

        A, B, C = False, False, False

        for i, j, k in triplets:
            if a == i and j <= b and k <= c: A = True
            if b == j and i <= a and k <= c: B = True
            if c == k and i <= a and j <= b: C = True

            if A and B and C: return True
        return False