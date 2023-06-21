class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int maxPeak = prices[prices.length-1];

        for(int i = prices.length-1; i >= 0; i--) {
            maxPeak = Math.max(maxPeak,prices[i]);
            profit = Math.max(profit, maxPeak - prices[i]);
        }

        return profit;
    }
}