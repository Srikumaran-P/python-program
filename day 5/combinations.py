class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans=[]
        def comb(i,mat):
            if len(mat)==k:
                ans.append(mat[:])
                return
            for j in range(i,n+1):
                mat.append(j)
                comb(j+1,mat)
                mat.pop()
        comb(1,[])
        return ans            




        
