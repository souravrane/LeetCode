class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            nums = set()
            for col in range(9):
                val = board[row][col]
                if val == ".": continue
                if val in nums: return False
                nums.add(val)
        
        for col in range(9):
            nums = set()
            for row in range(9):
                val = board[row][col]
                if val == ".": continue
                if val in nums: return False
                nums.add(val)
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                nums = set()
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        val = board[x][y]
                        if val == ".": continue
                        if val in nums: return False
                        nums.add(val)
                        
        return True