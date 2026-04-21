class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low = 0
        high = m*n-1
        while low<=high:
            mid = (low+high)//2
            i, j = mid//n, mid%n
            v = matrix[i][j]
            if v == target:
                return True
            elif v < target:
                low = mid + 1
            else:
                high = mid - 1
        return False