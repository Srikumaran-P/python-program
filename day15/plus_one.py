class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits = int("".join(map(str, digits)))

        new_digit = digits + 1
        new_digit = str(new_digit)

        new_digit2 = []

        for i in new_digit:
            new_digit2.append(int(i))

        return new_digit2
