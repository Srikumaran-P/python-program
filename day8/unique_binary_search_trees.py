class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * 20
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        if n <= 3:
            return dp[n]
        for j in range(4, n+1):
            result = 0
            for p in range(1, n+1):
                left = p-1
                right = j-p
                result += dp[left]*dp[right]
            dp[j] = result
        return dp[n]
