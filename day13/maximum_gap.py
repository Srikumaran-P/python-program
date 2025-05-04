class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<2:return 0
        nums.sort()
        a1=0
        for i in range(1,len(nums)):
            if a1<(nums[i]-nums[i-1]):
                a1=nums[i]-nums[i-1]
        return a1
        """
        :type nums: List[int]
        :rtype: int
        """
        
