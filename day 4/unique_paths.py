class Solution(object):
    def uniquePaths(self, m, n):
        oldrow=[1]*n
        for i in range(m-1):
            newRow=[1]*n
            for j in range(n-2,-1,-1):
                newRow[j]=newRow[j+1]+oldrow[j]
            oldrow=newRow
        return oldrow[0]
        
