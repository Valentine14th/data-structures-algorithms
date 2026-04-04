class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pos = {}
        maxx = 0
        for i, n in enumerate(nums):
            if n in pos:
                continue
            elif n+1 in pos and n-1 in pos:
                left = pos[n-1][0]
                right = pos[n+1][1]
            elif n-1 in pos:
                left = pos[n-1][0]
                right = n
            elif n+1 in pos:
                right = pos[n+1][1]
                left = n
            else:
                right = n
                left = n
            
            maxx = max(maxx, right-left+1)
            pos[left] = (left, right)
            pos[right] = (left, right)
        return maxx





        