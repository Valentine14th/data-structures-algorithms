class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        pre = 1
        suf = 1
        for i in range(len(nums)-1):
            suf = suf * nums[i]
            pre = pre * nums[len(nums)-1-i]
            prefix.append(suf)
            suffix.append(pre)
        print(prefix)
        print(suffix)
        out = []
        for i in range(len(nums)):
            if i == 0:
                out.append(suffix[-1])
            elif i == len(nums) - 1:
                out.append(prefix[-1])
            else:
                out.append(prefix[i-1] * suffix[-(i+1)])
        return out

        