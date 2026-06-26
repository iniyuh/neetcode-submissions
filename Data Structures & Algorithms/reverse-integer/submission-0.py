class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)[::-1]
        if x[-1] == '-': 
            print(x)
            x = '-' + x[:-1]
            print(x)

        ret = int(x)
        # ret = 0
        # mult = 1

        # for i in range(len(x)):
        #     val = int(x[i]) * mult

            
        return ret if -2 ** 31 <= ret <= 2 ** 31 - 1 else 0