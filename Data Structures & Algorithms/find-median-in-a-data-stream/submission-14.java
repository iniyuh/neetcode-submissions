class MedianFinder {
    private PriorityQueue<Integer> minHeap;
    private PriorityQueue<Integer> maxHeap;
    
    public MedianFinder() {
        minHeap = new PriorityQueue<>();
        maxHeap = new PriorityQueue<>(Collections.reverseOrder());
    }   
    
    public void addNum(int num) {
        if (maxHeap.size() == minHeap.size()) maxHeap.offer(num);
        else if (maxHeap.size() < minHeap.size()) maxHeap.offer(num);
        else minHeap.offer(num);

        if (maxHeap.size() > 0 && minHeap.size() > 0 && maxHeap.peek() > minHeap.peek()) {
            int lower = minHeap.poll(), higher = maxHeap.poll();
            maxHeap.offer(lower);
            minHeap.offer(higher);
        }
    }
    
    public double findMedian() {
        if (maxHeap.size() == minHeap.size()) return (maxHeap.peek() + minHeap.peek()) / 2.0;
        else if (maxHeap.size() < minHeap.size()) return (double) minHeap.peek();
        else return (double) maxHeap.peek();
    }
}
