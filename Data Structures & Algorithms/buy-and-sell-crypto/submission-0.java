class Solution {
    public int maxProfit(int[] prices) {
        int max_profit = 0;
        int current_min = Integer.MAX_VALUE;
        for(int price : prices){
            if(price < current_min){
                current_min = price;
            }
            if(price - current_min > max_profit){
                max_profit = price - current_min;
            }
        }
        return max_profit;
    }
}
