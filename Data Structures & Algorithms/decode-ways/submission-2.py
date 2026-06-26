class Solution:
    def numDecodings(self, s: str) -> int:
        hm = {}
        zerod = False

        def decode(string):
            if string in hm: return hm[string]
            elif string and string[0] == '0': return 0
            elif len(string) <= 1: return 1
            else:
                if string[1] == '0': 
                    if string[0] != '1' and string[0] != '2':
                        zerod = True
                        return 0

                    hm[string] = decode(string[2:])
                    return hm[string]
                else:
                    ret = decode(string[1:])
                    
                    if string[0] == '1' or ( string[0] == '2' and (int(string[1]) <= 6) ):
                        ret += decode(string[2:])

                    hm[string] = ret
                    return hm[string]
        
        return decode(s) if not zerod else 0