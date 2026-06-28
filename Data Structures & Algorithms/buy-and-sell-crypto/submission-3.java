class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) return 0;

        int maxProfit = 0;
        int currentMin = prices[0];
        
        for (int price : prices) {
            currentMin = Math.min(currentMin, price);
            maxProfit = Math.max(maxProfit, price - currentMin);
        }

        return maxProfit;
    }
}
