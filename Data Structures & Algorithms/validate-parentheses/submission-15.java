class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') stack.push(c);
            else {
                if (stack.size() == 0) return false;
                else if (c == ')') {
                    if (stack.peekFirst() != '(') return false;
                    else stack.pop();
                }
                else if (c == '}') {
                    if (stack.peekFirst() != '{') return false;
                    else stack.pop();
                }
                else if (c == ']') {
                    if (stack.peekFirst() != '[') return false;
                    else stack.pop();
                }
            }
        }

        return stack.size() == 0;
    }
}
