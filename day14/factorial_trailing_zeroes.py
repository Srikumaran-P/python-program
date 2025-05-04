class Solution(object):
    def trailingZeroes(self, n):
        def fact(n):
            if n == 0:
                return 1
            else:
                return n * fact(n - 1)

        factorial = fact(n)
        str_fact = str(factorial)
        zeros = 0

        for i in range(len(str_fact) - 1, -1, -1):
            if str_fact[i] == '0':
                zeros += 1
            else:
                break

        return zeros        
