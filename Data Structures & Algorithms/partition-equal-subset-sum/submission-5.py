class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dp[]
        #if len(nums) % 2 != 0:
        #    return False
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target // 2
        currDP = [False]*(target+1)
        currDP[0] = True
        for i in range(1, len(nums)+1):
            newDP = currDP.copy()
            for j in range(1, target+1):
                if j < nums[i-1]:
                    newDP[j] = currDP[j]
                else:
                    newDP[j] = currDP[j-nums[i-1]] or currDP[j]
            currDP = newDP
        return currDP[target]


        