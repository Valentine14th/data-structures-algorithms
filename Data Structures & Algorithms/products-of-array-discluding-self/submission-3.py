class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        for n in nums:
            pref.append(pref[-1]*n)
        print(pref)
        suf = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        print(suf)
        out = []
        for i in range(len(nums)):
            out.append(pref[i] * suf[i])
        return out

        