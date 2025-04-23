class Solution(object):
    def generateParenthesis(self, n):
        res=[]
        def helper(open, close, s):
            if open == close and open+close == n*2:
                res.append(s)
                return
            if open<n:
                helper(open+1, close, s+"(")
            if close < open:
                helper(open, close+1, s+")")
        helper(0, 0, "")
        return res
