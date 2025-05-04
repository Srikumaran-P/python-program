class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        mat=[]
        for i in tokens:
            if i=="+":
                a=mat.pop()
                b=mat.pop()
                ans=a+b
                mat.append(ans)
            elif i=="-":   
                a=mat.pop()
                b=mat.pop()
                ans=b-a 
                mat.append(ans)
            elif i=="*":   
                a=mat.pop()
                b=mat.pop()
                ans=a*b 
                mat.append(ans)
            elif i=="/":   
                a=mat.pop()
                b=mat.pop()
                ans=int(float(b)/a)
                mat.append(ans)
            else:
                mat.append(int(i))              
        return mat[0]
        
        

        
