class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # create a dictionary

        mapp = {1000:'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4:'IV', 1: 'I'}
        roman = ''
        
        for value in sorted(mapp.keys(), reverse=True): #for key, value in mapp.items(): this does not work in older python versions
            while num >= value:
                roman = roman + mapp[value]
                num -= value

        return roman
