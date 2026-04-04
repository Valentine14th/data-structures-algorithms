class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right: int = len(nums) - 1
        left: int = 0
        found = True
        mid = left + (right - left) // 2
        print("mid", mid)
        if nums[mid] > nums[left] and nums[mid] < nums[right] or len(nums) <= 1:
            print("no rotation")
            return self.binary(0, len(nums)-1, nums, target)
        while nums[mid-1] < nums[mid] and left < right:
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid - 1
            else:
                mid = left
                break
            mid = left + (right - left) // 2 
            #print("mid", mid, left, right)    
        print("rotation", mid)
        outl = self.binary(0, mid-1, nums, target)
        print("left okay")
        if outl != -1:
            return outl
        print("right?")
        return self.binary(mid, right, nums, target)

        
    def binary(self, left: int, right: int, nums: List[int], target: int) -> int:
        mid : int = left + (right - left) // 2
        while nums[mid] != target and left < right:
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            mid = left + (right - left) // 2
            print("mid search", mid, left, right)
        if nums[mid] == target:
            return mid
        else:
            return -1


        
        

            



        