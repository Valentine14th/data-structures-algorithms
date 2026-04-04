class Solution {
    public int climbStairs(int n) {
        int[] stairways = new int[n+1];
        stairways[n] = 1;
        stairways[n-1] = 1;
        for(int i = n-2; i >= 0; i--){
            stairways[i] = stairways[i+1] + stairways[i+2];
        }
        return stairways[0];
    }
}
