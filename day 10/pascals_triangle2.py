class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = {
            0: [1], 1: [1, 1], 2: [1, 2, 1]
        }

        output = result.get(rowIndex)
        if output:
            return output
        
        # Generate the target result
        for r in range(rowIndex+1):
            if r not in result:
                pl_output = result[(r-1)]
                new_output = [1]
                n = len(pl_output)
                for k in range(n//2):
                    new_output.append(pl_output[k]+pl_output[k+1])
                
                if n %2:
                    new_output += new_output[::-1]
                else:
                    new_output += new_output[-2::-1]
                result[r] = new_output
        return result.get(rowIndex)
