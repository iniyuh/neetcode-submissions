class MinStack {

    private int min;
    private Deque<List<Integer>> stack;

    public MinStack() {
        stack = new ArrayDeque<>();
    }
    
    public void push(int val) {
        int currMin = stack.size() == 0 ? val : Math.min(stack.peekFirst().get(1), val);
        stack.push(List.of(val, currMin));
    }
    
    public void pop() {
        stack.pop();
    }
    
    public int top() {
        return stack.peekFirst().get(0);
    }
    
    public int getMin() {
        return stack.peekFirst().get(1);
    }
}
