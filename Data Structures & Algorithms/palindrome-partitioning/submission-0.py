class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        
        def isPalindrome(arr):
            l, r = 0, len(arr) - 1

            while l < r:
                if arr[l] != arr[r]: return False
                l +=1
                r -= 1
            # print("".join(arr), "is palindrome")
            return True

        ret = []
        curr = []

        def helper(i):
            if i == len(s):
                if isPalindrome(curr[-1]): 
                    print("adding", curr)
                    ret.append([arr.copy() for arr in curr])
                    for arr in ret:
                        print(arr)
            else:
                if len(curr) == 0: 
                    curr.append([s[i]])
                    helper(i + 1)
                    curr.pop()
                else:
                    if isPalindrome(curr[-1]): 
                        curr.append([s[i]])
                        # print(curr)
                        helper(i + 1)
                        curr.pop()
                    
                    curr[-1].append(s[i])
                    helper(i + 1)
                    curr[-1].pop()


        helper(0)
        # print(ret)
        for i in range(len(ret)): ret[i] = ["".join(arr) for arr in ret[i]]
        return ret

