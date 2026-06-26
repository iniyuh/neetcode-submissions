class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for string in strs:
            encoded += str(len(string)) + '!' + string
        
        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        decoded = []
        currentStringLength = 0
        while i < len(s):
            char = s[i]

            if char != '!':
                currentStringLength += int(char)
                currentStringLength *= 10
                i += 1
            else:
                currentStringLength //= 10
                
                decoded.append(s[i + 1 : i + 1 + currentStringLength])
                i = i + 1 + currentStringLength

                currentStringLength = 0
        
        return decoded


