class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''

        for string in strs:
            s += str(len(string))
            s += '!'
            s += string
        
        print("encoded:", s)
        return s

    def decode(self, s: str) -> List[str]:
        ret = []

        i = 0

        while i < len(s):
            len_s = ''
            while s[i] != '!': 
                len_s += s[i]
                i += 1
            i += 1
            ret.append(s[i:i+int(len_s)])
            i += int(len_s)
        
        print("decoded:", ret)
        return ret
