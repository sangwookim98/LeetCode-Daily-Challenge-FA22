class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        # Base cases
        # no rows to make => return nothing
        if numRows == 0:
            return []
        
        # just 1st row => return 1 (2-D array)
        if numRows == 1:
            return [[1]]
        
        # Starting case: 
        res = [[1]]
        
        # for rows other than first row
        for x in range(1, numRows): 
            # Build a new row.
            row = []
            row.append(1)
            if x > 1:
                for y in range(1, x): 
                    row.append(lastRow[y] + lastRow[y - 1])
            row.append(1)
            
            lastRow = row
            
            res.append(list(row))
        
        return res