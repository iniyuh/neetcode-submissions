class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i):
            while i < len(s):
                num = int(s[i])
                nextNum = int(s[i+1]) if i + 1 < len(s) else None

                # print(num ,nextNum)

                if num == 0: return 0
                elif nextNum is not None:
                    if nextNum == 0:
                        # print("BANG", i)
                        if num <= 2:
                            i += 1
                        else: 
                            return 0
                    elif (
                        num == 2 and nextNum <= 6
                        or num == 1
                    ):
                        return dfs(i + 1) + dfs (i + 2)

                i += 1
            
            return 1
        
        return dfs(0)
