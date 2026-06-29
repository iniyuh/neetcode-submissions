class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int N = position.length;

        if (N == 0)
            return 0;

        int[][] pair = new int[N][2];

        for (int i = 0; i < N; i++) {
            pair[i][0] = position[i];
            pair[i][1] = speed[i];
        }

        Arrays.sort(pair, (a, b) -> Integer.compare(b[0], a[0]));

        System.out.println(pair[0][0] + " " + pair[0][1]);

        double maxTime = (double) (target - pair[0][0]) / pair[0][1];
        int fleets = 1;

        for (int i = 1; i < position.length; i++) {
            double time = (double) (target - pair[i][0]) / pair[i][1];
            System.out.println(time);
            if (time > maxTime) {
                maxTime = time;
                fleets++;
            }
        }

        return fleets;
    }
}
