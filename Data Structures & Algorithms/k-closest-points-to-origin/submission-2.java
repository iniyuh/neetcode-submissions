class Solution {
    private int dist(List<Integer> p) {
        int dx = Math.abs(p.get(0)), dy =Math.abs(p.get(1));
        return dx * dx + dy * dy;
    }

    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<List<Integer>> maxHeap = new PriorityQueue<>((a, b) -> Integer.compare(dist(b), dist(a)));

        for (int[] point : points) {
            maxHeap.offer(List.of(point[0], point[1]));

            if (maxHeap.size() > k) maxHeap.poll();
        }

        return maxHeap.stream().map(p -> new int[]{p.get(0), p.get(1)}).toArray(int[][]::new);
    }
}
