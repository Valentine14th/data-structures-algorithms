class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a : Dict[int, int] = {}
        for num in nums:
            if not a.get(num):
                a[num] = 1
            else:
                return True
        return False
        
         