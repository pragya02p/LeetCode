class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r=len(matrix)
        c=len(matrix[0])-1
        for i in range(r):
            if target>matrix[i][c]:
                continue
            else:
                for j in range(c+1):
                    if matrix[i][j]==target:
                        return True
        return False
        