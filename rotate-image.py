class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        sz = len(matrix)
        
        for row in range(sz):
            for col in range(row+1,sz):
                buff = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = buff
                
        for row in range(sz):
            for col in range(sz//2):                
                buff = matrix[row][col]
                matrix[row][col] = matrix[row][sz-1-col]
                matrix[row][sz-1-col] = buff