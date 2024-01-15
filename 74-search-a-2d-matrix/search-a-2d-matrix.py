class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0])-1
        while row < len(matrix) and col >= 0:
            num = matrix[row][col]
            if num == target:
                return True
            elif target < num:
                col -= 1
            else:
                row += 1
        return False

        