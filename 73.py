class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()
        
        for row_n in range(len(matrix)):
            for col_n in range(len(matrix[row_n])):
                if matrix[row_n][col_n]==0:
                    rows.add(row_n)
                    columns.add(col_n)
        
        for col_n in columns:
            for row_n in range(len(matrix)):
                matrix[row_n][col_n] = 0
        
        for row_n in rows:
            for col_n in range(len(matrix[row_n])):
                matrix[row_n][col_n] = 0
        return
