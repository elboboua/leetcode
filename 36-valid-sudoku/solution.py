from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set) 
        blocks = defaultdict(set)

        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell != ".":
                    if cell in cols[col] or cell in rows[row] or cell in blocks[(row//3, col//3)]:
                        return False
                    else:
                        cols[col].add(cell)
                        rows[row].add(cell)
                        blocks[(row//3, col//3)].add(cell)

        return True
    
# Valid board
board_1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# Not valid board
board_2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

sol = Solution()
print("Asserting two boards are correct")
assert sol.isValidSudoku(board_1) == True
assert sol.isValidSudoku(board_2) == False
print("passed")