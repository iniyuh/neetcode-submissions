class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += (str(len(s)))
            encoded += "%"
            encoded += s

        return encoded
    def decode(self, s: str) -> List[str]:
        ret = []

        anchor = 0
        i = 0

        while i < len(s):
            while s[i] != '%': i += 1
            length = int(s[anchor:i])

            i += 1

            ret.append( s[i:i+length] )

            i += length
            anchor = i
        
        return ret
