class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def hash_function(string):
            return ''.join(sorted(string))

        groups = {}
        for string in strs:
            index = hash_function(string)
            lst = groups.get(index)
            if lst:
                lst.append(string)
            else:
                lst = [string]
            groups.update({index : lst})

        output = []
        for key in groups.keys():
            output.append(groups[key])

        return output
