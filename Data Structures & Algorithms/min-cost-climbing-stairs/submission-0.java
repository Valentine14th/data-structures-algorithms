class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int steps = cost.length;
        int[] minCost = new int[steps+1];
        minCost[steps] = 0;
        minCost[steps-1] = cost[steps-1];
        for(int i = steps-2; i >= 0; i--){
            minCost[i] = 
                cost[i] +
                (minCost[i+1] < minCost[i+2] 
                ? minCost[i+1] : minCost[i+2]);
        }
        return (minCost[0] < minCost[1] 
                ? minCost[0] : minCost[1]);
        
    }
}
