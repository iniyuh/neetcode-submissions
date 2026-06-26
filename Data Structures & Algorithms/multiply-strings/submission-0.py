class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # if either is 0 return 0
        # otherwise set it up such that num1 is longer than (or same) as num2:
        #  8888
        #   777
        # we will loop over digits of num2 and multiply num1 by them, results stored as int
        # add all results together normally
        # cast sum to string and return

        if num1 == '0' or num2 == '0': return '0'

        if len(num1) < len(num2): num1, num2 = num2, num1


        ret = 0

        for mult2, digit2 in enumerate(reversed(num2)):
            carry = 0
            for mult1, digit1 in enumerate(reversed(num1)):
                digit1, digit2 = int(digit1), int(digit2)

                digit3 = digit1 * digit2 + carry
                carry = digit3 // 10
                digit3 = digit3 % 10

                ret += digit3 * (10 ** mult1) * (10 ** mult2)
            
            ret += carry * (10 ** len(num1) * (10 ** mult2))
        
        print(ret)
        return str(ret)





                




