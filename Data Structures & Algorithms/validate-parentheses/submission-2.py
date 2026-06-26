class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack: return False
                front = stack.pop()
                if (char == ')' and front != '(') or (char == ']' and front != '[') or (char == '}' and front != '{'):
                    return False
        return not stack