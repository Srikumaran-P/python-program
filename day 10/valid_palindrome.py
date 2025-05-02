class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleanText = ''.join(i for i in s if i.isalnum()).lower()
        normal = list(cleanText)
        reversed = list(normal)
        reversed.reverse()
        if normal == reversed:
            return True
        else:
            return False


        
