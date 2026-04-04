class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        let output = new Set()
        nums = nums.sort((a, b) => a - b)
        console.log(nums)
        for(let [i, num] of nums.entries()){
            let left = i == 0 ? 1 : 0
            let right = i == nums.length-1 ? nums.length-2 : nums.length-1
            while((left < right)){
                if(nums[left]+nums[right] < -num){
                    left = left+1 == i ? left+2: left+1
                }
                else if(nums[left]+nums[right] > -num){
                    right = right-1 == i ? right-2 : right-1
                }
                else{
                    //console.log([num, nums[left], nums[right], i, left, right])
                    output.add(JSON.stringify([num, nums[left], nums[right]].sort()))
                    left = left+1 == i ? left+2: left+1
                }
            }
        }
        let out = []
        for(let a of output){
            out.push(JSON.parse(a))
        }
        return out
    }
}
