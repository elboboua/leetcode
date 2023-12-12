class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        for row in matrix:
            if row[-1] < target:
                continue
            left, right = 0, len(row)-1
            while left <= right:
                mid = (left+right)//2
                num = row[mid]
                if num == target:
                    return True
                elif num > target:
                    right = mid -1                
                else:
                    left = mid + 1
        
        return False

sol = Solution()

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
assert sol.searchMatrix(matrix, target) == True
print("Passed")
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
assert sol.searchMatrix(matrix, target) == False
print("Passed")