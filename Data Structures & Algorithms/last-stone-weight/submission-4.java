class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());

        for (int stone : stones) maxHeap.offer(stone);

        while (maxHeap.size() > 1) {
            int x = maxHeap.poll();
            int y = maxHeap.poll();
            int remainder = Math.abs(x - y);

            if (remainder != 0) maxHeap.offer(remainder);
        }

        return maxHeap.size() == 1 ? maxHeap.poll() : 0;
    }
}
