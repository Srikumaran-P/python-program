class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s[::-1]
        words = s.split()
        new = []

        for i in words:
            new.append(i[::-1])

        return " ".join(new)
