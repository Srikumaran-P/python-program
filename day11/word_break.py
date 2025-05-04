class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """ 
        
        word=set(wordDict)
        mat=[False]*(len(s)+1)
        mat[0]=True

        for i in range(1,len(s)+1):
            for j in range(i):
              if mat[j] and s[j:i] in word:
                mat[i]=True
                break
        return mat[-1]        

                    





        
