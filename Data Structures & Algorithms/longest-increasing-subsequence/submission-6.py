class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp i, j last, means increasing seq from i with last values j
        # so when i == j, then always 1
        dp = [-1]*len(nums)
        dp[-1] = 1
        for i in range(len(nums)-1, -1, -1):
            maxi = 1
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    maxi = max(maxi, dp[j]+1)
            dp[i] = maxi
        return max(dp)

                
                


        

            

        