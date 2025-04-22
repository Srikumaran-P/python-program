class Solution(object):
    def myAtoi(self, s):

        if s == '':
            return 0

        i = 0
        while i <= len(s)-1 and s[i] == ' ':
            i += 1

        if i == len(s):
            return 0

        if (s[i] < "0" or s[i] > "9") and (s[i] != '-') and (s[i] != '+'):
            return 0
        if (i+1 <= len (s)-1) and (s[i] == '-' or s[i] == '+') and (s[i+1] == '-' or s[i+1] == '+'):
            return 0

        n = ""
        if s[i] == '-' or s[i] == '+':
            n += s[i]
            i += 1

        while i <= len(s)-1 and s[i] >= "0" and s[i] <= "9":
            n += s[i]
            i += 1

        if n == '' or n == '-' or n == '+':
            return 0
        elif int(n) < -2 ** 31:
            return -2 ** 31
        elif int(n) > 2 ** 31 -1:
            return 2 ** 31 -1
        else:
            return int(n) 
