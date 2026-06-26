class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        
        def helper():
            number = 0
            string = ''

            while self.i < len(s):            
                char = s[self.i]

                if char.isdigit():
                    number *= 10
                    number += int(char)
                elif char == '[':
                    self.i += 1
                    string += (number * helper())
                    number = 0
                elif char == ']':
                    print(string)
                    return string
                else:
                    string += char
            
                self.i += 1
            return string
                
        return helper()