class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best = 0
        while left < right:
            leftHighest = heights[left] > heights[right]
            area = min(heights[left], heights[right]) * (right - left)
            if area > best:
                best = area
            if not leftHighest:
                nex = left 
                while heights[nex] <= heights[left]:
                    print(nex, left, right)
                    if nex >= right:
                        print("exit left")
                        return best
                    else:
                        nex = nex + 1
                left = nex
            else:
                nex = right 
                while heights[nex] <= heights[right]:
                    if nex <= left:
                        print("exit right")
                        return best
                    nex = nex - 1
                right = nex
        return best

            

        

        