class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        test = numbers[l] + numbers[r]
        while test != target:
            if test > target:
                r -= 1
            else:
                l += 1
            test = numbers[l] + numbers[r]
        return [l+1, r+1]


        