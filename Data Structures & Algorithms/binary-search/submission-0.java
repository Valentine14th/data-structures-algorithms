class Solution {
    public int search(int[] nums, int target) {
        int left_index = 0;
        int right_index = nums.length - 1;
        int current_index = nums.length/2;
        int current = nums[current_index];
        while(left_index <= right_index){
            if(target > current){
                left_index = current_index + 1;
            }
            else if (target < current){
                right_index = current_index - 1;
            }
            else{
                return current_index;
            }
            current_index = (right_index + left_index)/2;
            current = nums[current_index];
        }
        return -1;
    }
}
