class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}
        maxRank = 0

        for num in nums:
            if num not in hm:
                rank = 1 + hm.get(num+1, [0])[0]
                maxRank = max(maxRank, rank)
                child = num + rank - 1

                par = hm[num - 1][1] if num - 1 in hm else num
                if par != num: 
                    hm[par][0] += rank
                    maxRank = max(maxRank, hm[par][0])
                    print(par, hm[par])
                
                if child != num: hm[child][1] = par
                
                hm[num] = [rank, par]
                print(num, hm[num])
                if child != num: print(child, hm[child])
                print()
        
        return maxRank
            
                    

