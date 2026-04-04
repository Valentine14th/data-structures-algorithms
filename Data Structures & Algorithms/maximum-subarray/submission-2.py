class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out = [[float("-inf") for _ in range(len(nums))] for _ in range(len(nums))]
        maxval = float("-inf")
        maxind = (-1, -1)
        for i in range(len(nums)):
            summ = 0
            for j in range(i, len(nums)):
                if i == 0:
                    summ += nums[j]
                    out[i][j] = summ
                    if out[i][j] > maxval: 
                        maxval = out[i][j]
                        maxind = i, j
                else:
                    out[i][j] = out[0][j] - out[0][i-1]
                    if out[i][j] > maxval: 
                        maxval = out[i][j] 
                        maxind = i, j 
        print(out)
        return maxval


        
        