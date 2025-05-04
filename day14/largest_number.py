class Solution(object):
    def largestNumber(self, nums):
        lst = []
        for i in nums:
            i = str(i)
            lst.append(i)

        res = ""
        while len(lst) != 0:
            max = ""
            for i in lst:
                if max == "" or (i + max > max + i):
                    max = i

            res += max
            lst.remove(max)

        if res[0] == "0":
            return "0"

        return res
