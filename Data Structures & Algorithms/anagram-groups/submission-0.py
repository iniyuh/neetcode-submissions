class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1: return [strs]

        hm = defaultdict(list)

        def calcBuckets(string):
            buckets = [0] * 26

            for char in string:
                buckets[ord(char) - ord('a')] += 1
            
            return str(buckets)

        for string in strs:
            key = calcBuckets(string)
            hm[key].append(string)
        
        return list(hm.values())