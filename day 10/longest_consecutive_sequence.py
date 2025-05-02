class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_length = 0
        
        nums_set = set(nums) #O(1) look up ,useful for later.

        for x in nums_set:
            if x-1 not in nums_set:
                current = x
                count = 1

                while current+1 in nums_set:
                    current+=1
                    count+=1
                
                max_length = max(max_length,count)

        return max_length

        
