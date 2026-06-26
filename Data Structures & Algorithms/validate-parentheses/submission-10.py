class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left_brackets = ['(', '{', '[']

        for char in s:
            if char in left_brackets: stack.append(char)
            else:
                if not stack: return False

                top = stack.pop()
                if not( ( char == ')' and top == '(' ) or ( char == '}' and top == '{' ) or ( char == ']' and top == '[' ) ): return False

        return len(stack) == 0
