class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token in ops:
                val2, val1 = stack.pop(), stack.pop()

                match token:
                    case '+':
                        stack.append(val1 + val2)
                    case '-':
                        stack.append(val1 - val2)
                    case '*':
                        stack.append(val1 * val2)
                    case '/':
                        val = val1 / val2
                        if val < 0: stack.append(math.ceil(val))
                        else: stack.append(math.floor(val))
            else: stack.append(float(token))
        
        return int(stack.pop())