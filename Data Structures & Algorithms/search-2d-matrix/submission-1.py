class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        height = len(matrix)
        width = len(matrix[0])
        left = 0
        right = height - 1
        while left <= right:
            curr = (left + right) // 2
            print(curr)
            if matrix[curr][-1] >= target and matrix[curr][0] <= target:
                print("found row")
                break
            if matrix[curr][0] > target:
                print("too big")
                right = curr - 1
            elif matrix[curr][-1] < target:
                print("too small")
                left = curr + 1
        correct_row = matrix[curr]
        left = 0
        right = width - 1
        while left <= right:
            curr =  (left + right) // 2
            if correct_row[curr] < target:
                left = curr + 1
            elif correct_row[curr] > target:
                right = curr - 1
            elif correct_row[curr] == target:
                return True
        return False


                
            


        