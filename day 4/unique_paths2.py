class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        obstacleGrid[0][0]=1
        for i in range(1,m):
            obstacleGrid[i][0]=int(obstacleGrid[i-1][0] and not obstacleGrid[i][0])
        for j in range(1,n):
            obstacleGrid[0][j]=int(obstacleGrid[0][j-1] and not obstacleGrid[0][j])
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    obstacleGrid[i][j]+=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j]=0
        return obstacleGrid[-1][-1] 
