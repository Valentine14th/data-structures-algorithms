class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()

        for k in range(len(nums)):
            want = {}

            for i in range(len(nums)):
                if i == k:
                    continue

                if nums[i] in want:
                    j = want[nums[i]]
                    if j != k:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        out.add(triplet)

                want[-nums[k] - nums[i]] = i

        return [list(t) for t in out]