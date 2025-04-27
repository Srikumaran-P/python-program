class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_lst = path.split('/')
        stack = []
        result = ""
        for p in path_lst:
            if p not in ["", "..", "."]:
                stack.append(p)
            elif p == ".." and stack:
                stack.pop()
        if not stack:
            return "/"
        else: 
            while stack:
                result = "/"+stack.pop()+result
        return result

        
