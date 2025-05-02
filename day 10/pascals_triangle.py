class Solution(object):
    def generate(self, numRows):
        res = []
        for item in range(numRows):
            if item == 0:
                res.append([1])
            else:
                row = [1] * (item + 1)
                for i in range(1,item):
                    row[i] = res[item - 1][i - 1] + res[item - 1][i]
                res.append(row) 
        return res

sol = Solution()
print(sol.generate(5))  
