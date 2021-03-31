from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print(len(matrix))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True

        return False
if __name__ =='__main__':
    s = Solution()
    print(s.searchMatrix([[1]],1))