class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        curr = []
        ret = []

        def helper(i):
            if i == len(digits): ret.append("".join(curr))
            else:
                for letter in mapping[digits[i]]:
                    curr.append(letter)
                    helper(i + 1)
                    curr.pop()
        
        helper(0)
        return ret




