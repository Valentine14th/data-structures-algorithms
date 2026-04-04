class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tot = sum(nums)
        should = 0
        for i in range(len(nums)+1):
            should += i
        print(should)
        return should - tot

        