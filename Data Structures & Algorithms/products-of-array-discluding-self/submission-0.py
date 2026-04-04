class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = []
        for index, i in enumerate(nums):
            if i == 0:
                zeros.append(index)
            else:
                prod *= i
        if len(zeros) > 1:
            out = [0 for i in nums]
        elif len(zeros) == 1:
            out = [0 if index != zeros[0] else prod for index, i in enumerate(nums)]
        else:
            out = [int(prod / i) for i in nums]
        return out

        