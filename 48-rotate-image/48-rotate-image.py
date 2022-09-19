class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l=len(matrix)
        lt=[]
        for i in range(l):
            lt.append(matrix[i][0:l])
        print(lt)
        for i in range(l-1,-1,-1):
            t=lt.pop(0)
            for j in range(l):
                matrix[j][i]=t[j]
                
                