class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini = 1
        maxi = 1
        res = nums[0]
        for n in nums:
            c_max = maxi
            maxi = max(n, c_max*n, mini*n)
            mini = min(n, c_max*n, mini*n)
            res = max(res, maxi)
        return res


            
        