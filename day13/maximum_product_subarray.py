class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0


        maxpr = nums[0]
        res = nums[0]
        minpr = nums[0]

        for num in nums[1:]:

            if num<0:
                maxpr , minpr = minpr, maxpr

            maxpr = max(maxpr*num, num)
            minpr = min(minpr*num, num)

            res = max(res, maxpr)

        return res

        
            
        
            


            
