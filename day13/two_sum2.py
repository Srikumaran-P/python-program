class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0 
        right = len(numbers) - 1

        while (left < right) :
            Sum = numbers[left] + numbers[right]

            if (Sum == target) :
                return ([left+1 , right+1])
                
            elif (Sum < target) :
                left += 1
            else :
                right -= 1

        return []
        
