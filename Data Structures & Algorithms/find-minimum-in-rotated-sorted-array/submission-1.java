class Solution {
    public int findMin(int[] nums) {
        int lefti = 0;
        int righti = nums.length - 1;
        int midi = nums.length / 2;

        if (nums.length == 1){
            return nums[0];
        }
        
        while(true){
            // if the number right of mid is smaller, right is smallest
            if(nums[midi] > nums[(midi+1)%nums.length]){
                return nums[(midi+1)%nums.length];
            }
            // if the number left of mid is bigger, mid is smallest
            else if(nums[midi-1 < 0 ? nums.length - 1 : midi-1] > nums[midi]){
                return nums[midi];
            }
            // this is a sorted segment on the right
            // so the split must be left
            if (nums[midi] < nums[righti]){
                righti = midi;
                midi = (lefti + righti) / 2;
            }
            // sorted on the left
            else if (nums[midi] > nums[lefti]){
                lefti = midi;
                midi = (lefti + righti) / 2;
            }
        }
        
    }
}
