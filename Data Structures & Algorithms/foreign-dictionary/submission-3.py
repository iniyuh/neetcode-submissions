class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        before = defaultdict(list)
        charSet = set(words[0])

        for i in range(len(words) - 1):
            wordA, wordB = words[i], words[i+1]
            L = min(len(wordA), len(wordB))

            charSet.update(set(wordB))

            j = 0
            while j < L and wordA[j] == wordB[j]: j += 1
            
            if j != L: 
                before[wordB[j]].append(wordA[j])
            elif L == len(wordB) != len(wordA): return ''

        print(before)
        print(charSet)


        ret = ''
        visited = set()
        cycle = set()

        def dfs(char):
            if char in cycle: return False
            elif char in visited: return True

            cycle.add(char)

            for pre in before[char]:
                if not dfs(pre): return False
            
            cycle.remove(char)
            visited.add(char)
            nonlocal ret
            ret += char
            return True

        
        while charSet:
            if not dfs(charSet.pop()): return ''

        return ret