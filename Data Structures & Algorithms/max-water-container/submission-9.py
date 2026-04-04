class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            maxi = max(maxi, min(heights[left], heights[right])*(right-left)) 
            if heights[left] <= heights[right]:
                h = heights[left]
                left += 1
                while left < len(heights) and heights[left] < h:
                    left += 1
            #elif heights[left] >= heights[right]:
            else:
                h = heights[right]
                right -= 1
                while right > 0 and heights[right] < h:
                    right -= 1
        print(left, right)
        return maxi
        