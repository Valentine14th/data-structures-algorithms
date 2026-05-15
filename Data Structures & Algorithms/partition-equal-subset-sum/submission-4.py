class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dp[]
        #if len(nums) % 2 != 0:
        #    return False
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2
        dp = [[False]*(target+1) for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            dp[i][0] = True
        currsum = 0
        for i in range(1, len(nums)+1):
            #currsum = currsum + nums[i]
            #tar = currsum // 2
            for j in range(1, target+1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
        return dp[len(nums)][target]


        