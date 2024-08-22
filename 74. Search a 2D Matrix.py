class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find correct row
        l = 0
        r = len(matrix) - 1
        row = len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[mid][-1]:
                return True
            if  matrix[mid][0] <= target < matrix[mid][-1]:
                row = mid
                break
            if target > matrix[mid][-1] and target > matrix[mid][0]:
                l = mid + 1
            else:
                r = mid - 1 
        
        # do binary search in row
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False