class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        summ = 0
        left = 0
        right = 0
        out = []

        # right is the NEXT index to include in the window [left, right)
        while right < n:
            # 1) expand window by adding nums[right]
            summ += nums[right]
            right += 1

            # 2) while sum is big enough, record length and shrink from left
            while summ >= target:
                out.append(right - left)
                summ -= nums[left]
                left += 1

        return min(out) if out else 0
